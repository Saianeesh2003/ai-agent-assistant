# 🤖 AI Agent Assistant

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-agent-assistant-saianeesh2003.streamlit.app)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> An intelligent AI agent powered by Google Gemini 2.0 that can perform tasks, fetch real-time data, create files, and build web applications autonomously.



## ✨ Features

- 🌤️ **Real-time Weather Data** - Fetch current weather for any city worldwide
- 📝 **Automated File Creation** - Generate and create files programmatically
- 🌐 **Web App Builder** - Build complete HTML/CSS/JS applications on demand
- 🧠 **Intelligent Agent Loop** - Implements Plan → Action → Observe → Finish pattern
- 💬 **Interactive Chat Interface** - Beautiful Streamlit-powered UI
- 📁 **File Management** - Preview and download created files directly
- 🔄 **Multi-step Reasoning** - Agent thinks through complex tasks step-by-step

## 🚀 Live Demo

Try it out here: https://ai-agent-assistant-saianeesh.streamlit.app/



## 📋 Table of Contents

- [Installation](#-installation)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Architecture](#-architecture)
- [Example Queries](#-example-queries)
- [Technologies Used](#-technologies-used)
- [Configuration](#-configuration)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

## 💻 Installation

### Prerequisites

- Python 3.12 or higher
- Google Gemini API key ([Get it here](https://makersuite.google.com/app/apikey))

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Saianeesh2003/ai-agent-assistant.git
   cd ai-agent-assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   
   Navigate to `http://localhost:8501`

## 🎯 Usage

### Basic Commands

1. **Ask Questions**
   ```
   "Write Python code to add two numbers"
   ```

2. **Get Weather Information**
   ```
   "What's the weather in Tokyo?"
   ```

3. **Create Files**
   ```
   "Create a simple HTML page with a gradient background"
   ```

4. **Build Applications**
   ```
   "Build a working todo list web app"
   ```

### Using Example Queries

Click any of the example query buttons in the sidebar to quickly test the agent's capabilities.

### Downloading Created Files

1. Files appear in the sidebar under "📁 Created Files"
2. Click on a file to preview its content
3. Use the download button to save files locally
4. For web apps, download all files and open `index.html` in your browser

## 🧠 How It Works

The AI Agent follows an autonomous loop:

```
1. PLAN    → Analyzes the user's request and creates a strategy
2. ACTION  → Executes tools (weather API, file creation, etc.)
3. OBSERVE → Processes results and decides next steps
4. FINISH  → Delivers the final answer
```

### Agent Loop Diagram

```
┌─────────────┐
│ User Query  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   PLAN      │ ◄─────┐
└──────┬──────┘       │
       │              │
       ▼              │
┌─────────────┐       │
│   ACTION    │       │
│  (Use Tool) │       │
└──────┬──────┘       │
       │              │
       ▼              │
┌─────────────┐       │
│   OBSERVE   │       │
│  (Results)  │       │
└──────┬──────┘       │
       │              │
       ▼              │
    [Done?] ──No─────┘
       │
       Yes
       ▼
┌─────────────┐
│   FINISH    │
│  (Answer)   │
└─────────────┘
```

## 🏗️ Architecture

### Tech Stack

- **Frontend**: Streamlit (Python web framework)
- **AI Model**: Google Gemini 2.0 Flash
- **APIs**: wttr.in (Weather data)
- **Language**: Python 3.12+

### Project Structure

```
ai-agent-assistant/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not in repo)
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

### Available Tools

| Tool | Description | Input Format |
|------|-------------|--------------|
| `get_weather` | Fetches real-time weather data | City name (string) |
| `create_file` | Creates files with specified content | `filename\|content` |

## 💡 Example Queries

### Weather Information
```
"What's the weather in Paris?"
"How's the temperature in Mumbai?"
```

### Code Generation
```
"Write Python code to add two numbers"
"Create a function to reverse a string"
```

### Web Development
```
"Create a simple HTML page with a blue background"
"Build a calculator webpage"
"Make a todo list app with HTML, CSS, and JavaScript"
```

### File Creation
```
"Create a file called notes.txt with my shopping list"
"Generate a Python script for data processing"
```

## 🛠️ Technologies Used

- **[Streamlit](https://streamlit.io/)** - Web framework for data apps
- **[Google Gemini 2.0](https://deepmind.google/technologies/gemini/)** - Large Language Model
- **[Python-dotenv](https://pypi.org/project/python-dotenv/)** - Environment variable management
- **[Requests](https://requests.readthedocs.io/)** - HTTP library

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Your Google Gemini API key | Yes |

### Customization

You can extend the agent by adding new tools in the `available_tools` dictionary:

```python
def my_custom_tool(input_str: str):
    # Your tool logic here
    return result

available_tools = {
    "get_weather": get_weather,
    "create_file": create_file,
    "my_custom_tool": my_custom_tool  # Add your tool
}
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions

- [ ] Add more tools (calculator, web scraper, database queries)
- [ ] Implement conversation memory
- [ ] Add support for image generation
- [ ] Create unit tests
- [ ] Improve error handling
- [ ] Add logging functionality

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

**Saianeesh** 
- GitHub: [@Saianeesh2003](https://github.com/Saianeesh2003)
- Project Link: [https://github.com/Saianeesh2003/ai-agent-assistant](https://github.com/Saianeesh2003/ai-agent-assistant)

## 🙏 Acknowledgments

- [Google Gemini](https://deepmind.google/technologies/gemini/) for the powerful AI model
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [wttr.in](https://wttr.in/) for weather data API
- The open-source community for inspiration and support

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Saianeesh2003/ai-agent-assistant&type=Date)](https://star-history.com/#Saianeesh2003/ai-agent-assistant&Date)

---

<div align="center">

**Made with ❤️ by Saianeesh**

If you found this project helpful, please consider giving it a ⭐!

[Report Bug](https://github.com/Saianeesh2003/ai-agent-assistant/issues) · [Request Feature](https://github.com/Saianeesh2003/ai-agent-assistant/issues)

</div>
