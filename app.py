from dotenv import load_dotenv
from anthropic import Anthropic
import os
import requests
import json
import streamlit as st

load_dotenv()

# ============ PAGE CONFIG ============
st.set_page_config(
    page_title="AI Agent Assistant",
    page_icon="🤖",
    layout="wide"
)

# ============ INITIALIZE SESSION STATE ============
if "messages" not in st.session_state:
    st.session_state.messages = []
if "created_files" not in st.session_state:
    st.session_state.created_files = []
if "example_query" not in st.session_state:
    st.session_state.example_query = None

# ============ GET CLIENT ============
@st.cache_resource
def get_client():
    api_key = os.environ.get("CLAUDE_API_KEY")
    if not api_key:
        st.error("⚠️ API_KEY not found! Please check your .env file")
        st.stop()
    return Anthropic(api_key=api_key)

client = get_client()

# ============ HELPER FUNCTIONS ============
def clean_json(text):
    text = text.strip()
    if text.startswith("```json"):
        text = text[7:]
    if text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()

def get_weather(city: str):
    url = f"https://wttr.in/{city}?format=%C+%t"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return f"The weather in {city} is {response.text.strip()}."
    except Exception as e:
        return f"Error fetching weather: {e}"
    return "Something went wrong"

def create_file(args_str: str):
    try:
        if "|" not in args_str:
            return "Error: Input must be in format 'filename|content'"
            
        filename, content = args_str.split("|", 1)
        filename = os.path.basename(filename.strip()) 
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        
        # Store file info in session state
        st.session_state.created_files.append({
            "name": filename,
            "content": content
        })
            
        return f"Successfully created file: {filename}"
    except Exception as e:
        return f"Error creating file: {e}"

available_tools = {
    "get_weather": get_weather,
    "create_file": create_file
}

SYSTEM_PROMPT = """
You are an AI Agent. You work in a loop: Plan -> Action -> Observe -> Finish.

IMPORTANT RULES:
1. If the user asks a simple question that doesn't need tools (like "write code for X", "explain Y", "help me with Z"), go DIRECTLY to "finish" step with your answer. DO NOT use tools for simple questions.
2. ONLY use tools when you need to: fetch weather, create actual files, or perform external actions.
3. Output ONLY raw JSON. Do NOT wrap it in markdown code blocks.
4. For web apps: Create COMPLETE, WORKING files with ALL necessary code. Don't create placeholder or incomplete files and ensure the primary goal is to create visually stunning, highly polished, and responsive web pages suitable for desktop browsers.
5. Prioritize clean, modern design and intuitive user experience.
6. For simple HTML/CSS/JS apps: Create self-contained files that work when opened directly.
7. Action Step: Use 'create_file' tool. Input format: "filename|code_content".
8. Accuracy & Detail: Strive for technical accuracy and adhere to detailed specifications (e.g., Tailwind classes, CSS properties).
9. If user asks who you are, tell them you are a helpful assistant developed by Sai Aneesh.
10. You are an expert in Mathematics as well.
11.You can write code for React for interactive UI,as well handle backend developement like NodeJS and NextJS,you are an expert experienced Senior Full Stack Developer who can handle all these:
HTML,CSS,Tailwind CSS,JavaScript, cutting-edge backend technologies:Node.js, Express, Mongoose,Prisma, Drizzle, PostgreSQL, NeonDB,
 Frontend Mastery with React which includes:
 React fundamentals,API handling,State management with Redux, Toolkit, and Zustand

 finally  you’ll combine everything  to build full-stack applications. Plus,  get a sneak peek into AI and machine learning:
Explore TensorFlow.js
Experiment with Langchain for AI-driven web apps


Output JSON Format:
{
    "step": "plan" | "action" | "observe" | "finish",
    "content": "Your thought or answer",
    "function": "tool_name (only for action step)",
    "input": "tool input (only for action step)"
}

Examples:
- "give me python code to add numbers" → step: "finish", content: "Here's the code..."
- "what's the weather?" → step: "action", function: "get_weather"
- "create a todo app" → step: "action", function: "create_file"
"""

# ============ AGENT FUNCTION ============
def run_agent_streamlit(user_query):
    """Run your agent with Streamlit UI"""
    
    # Initialize conversation history for Claude
    conversation_history = []
    
    # Create container for status updates
    status_container = st.container()
    
    for i in range(15):
        try:
            # Build messages for Claude API
            if not conversation_history:
                # First message
                messages = [{"role": "user", "content": user_query}]
            else:
                # Continue conversation
                messages = conversation_history
            
            # Call Claude API
            response = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=2000,
                system=SYSTEM_PROMPT,
                messages=messages
            )
            
            # Extract response text
            response_text = response.content[0].text
            
            # Clean and parse response
            cleaned_text = clean_json(response_text)
            
            try:
                ai_data = json.loads(cleaned_text)
            except json.JSONDecodeError:
                st.warning("⚠️ Invalid JSON received, retrying...")
                conversation_history.append({"role": "assistant", "content": response_text})
                conversation_history.append({"role": "user", "content": "Error: Invalid JSON format. Please output valid JSON only."})
                continue

            step = ai_data.get("step")
            content = ai_data.get("content", "")
            
            # Display step in Streamlit
            with status_container:
                if step == "plan":
                    st.info(f"🧠 **Planning:** {content[:200]}...")
                elif step == "action":
                    func_name = ai_data.get("function", "unknown")
                    st.warning(f"⚡ **Action:** Using tool `{func_name}`")
                elif step == "observe":
                    st.success(f"👀 **Observation:** {content[:150]}...")

            # Add to conversation history
            conversation_history.append({"role": "assistant", "content": response_text})

            # Check if finished
            if step == "finish":
                return content

            # Execute action
            elif step == "action":
                func_name = ai_data.get("function")
                func_input = ai_data.get("input")

                if func_name in available_tools:
                    tool_result = available_tools[func_name](func_input)
                    
                    observation_json = json.dumps({
                        "step": "observe",
                        "content": tool_result
                    })
                    
                    conversation_history.append({"role": "user", "content": observation_json})
                else:
                    error_msg = f"Error: Tool '{func_name}' not found. Available tools: {list(available_tools.keys())}"
                    conversation_history.append({"role": "user", "content": error_msg})

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            return "An error occurred while processing your request."
    
    return "Agent completed processing."

# ============ UI LAYOUT ============
st.title("🤖 AI Agent Assistant")
st.markdown("### Powered by Claude ")

# Sidebar
with st.sidebar:
    st.header("📖 About This Agent")
    st.markdown("""
    This AI Agent can:
    - 🌤️ **Get weather** information
    - 📝 **Create files** automatically
    - 🌐 **Build web apps** (HTML/CSS/JS)
    - 💡 **Answer questions** directly
    - 🧮 **Write code** for you
    
    **How it works:**
    1. Type your request below
    2. Watch the agent think
    3. Get your results!
    """)
    
    st.divider()
    
    st.header("💡 Example Queries")
    
    examples = [
        "What's the weather in Tokyo?",
        "Write Python code to add two numbers",
        "Create a simple HTML page with a gradient",
        "Build a working todo list app"
    ]
    
    for example in examples:
        if st.button(example, key=f"btn_{example}", use_container_width=True):
            st.session_state.example_query = example
    
    st.divider()
    
    # Show created files
    if st.session_state.created_files:
        st.header("📁 Created Files")
        st.info(f"✅ {len(st.session_state.created_files)} file(s) created")
        
        for file in st.session_state.created_files:
            with st.expander(f"📄 {file['name']}"):
                # Show preview
                if len(file['content']) > 1000:
                    st.code(file['content'][:1000] + "\n\n... (truncated)")
                else:
                    st.code(file['content'])
                
                # Download button
                st.download_button(
                    label=f"⬇️ Download {file['name']}",
                    data=file['content'],
                    file_name=file['name'],
                    mime="text/html" if file['name'].endswith('.html') else "text/plain",
                    key=f"download_{file['name']}_{len(st.session_state.created_files)}"
                )
        
        # Instructions
        st.markdown("---")
        st.markdown("""
        **📖 How to use:**
        1. Download all files
        2. Put them in one folder
        3. Double-click `index.html`
        """)
    
    st.divider()
    
    if st.button("🗑️ Clear Everything", use_container_width=True):
        st.session_state.messages = []
        st.session_state.created_files = []
        st.rerun()

# ============ DISPLAY CHAT HISTORY ============
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ============ HANDLE INPUT ============
# Always show chat input (must be outside if/else)
user_input = st.chat_input("Ask the agent anything... 💬")

# Check if example button was clicked (overrides typed input)
if "example_query" in st.session_state and st.session_state.example_query:
    user_input = st.session_state.example_query
    st.session_state.example_query = None  # Clear immediately

# Process user input (from chat or example button)
if user_input:
    # Clear previous created files for new query
    files_before = len(st.session_state.created_files)
    
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Run agent and display response
    with st.chat_message("assistant"):
        with st.spinner("🤔 Agent is thinking..."):
            result = run_agent_streamlit(user_input)
        st.markdown(result)
        
        # Show success message if files were created
        files_after = len(st.session_state.created_files)
        if files_after > files_before:
            new_files = files_after - files_before
            st.success(f"✅ {new_files} file(s) created! Check the sidebar to download them.")
    
    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": result})

# Footer
st.divider()
st.caption("🎈 Built with Streamlit | Powered by Claude ")