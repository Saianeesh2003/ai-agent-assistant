# 🤖 AI Agent Assistant

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-agent-assistant-saianeesh.streamlit.app/)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Powered by Claude](https://img.shields.io/badge/Powered%20by-Claude%20Sonnet%204-blueviolet)](https://www.anthropic.com/claude)

> An intelligent AI agent powered by Claude  that can perform tasks, fetch real-time data, create files, and build web applications autonomously.

## ✨ Features

- 🌤️ **Real-time Weather Data** - Fetch current weather for any city worldwide
- 📝 **Automated File Creation** - Generate and create files programmatically
- 🌐 **Web App Builder** - Build complete HTML/CSS/JS applications on demand
- 🧠 **Intelligent Agent Loop** - Implements Plan → Action → Observe → Finish pattern
- 💬 **Interactive Chat Interface** - Beautiful Streamlit-powered UI
- 📁 **File Management** - Preview and download created files directly
- 🔄 **Multi-step Reasoning** - Agent thinks through complex tasks step-by-step
- 🎨 **Modern Design** - Polished, responsive web pages with excellent UX

## 🚀 Live at:  **[AI Agent Assistant](https://ai-agent-assistant-saianeesh.streamlit.app/)**

Video Demo: https://youtu.be/vH32fq1o4v4

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
- Anthropic Claude API key ([Get it here](https://console.anthropic.com/settings/keys))

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
   ANTHROPIC_API_KEY=your_api_key_here
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
   "Explain quantum computing"
   ```

2. **Get Weather Information**
   ```
   "What's the weather in Tokyo?"
   "How's the temperature in London?"
   ```

3. **Create Files**
   ```
   "Create a simple HTML page with a gradient background"
   "Make a Python script for data analysis"
   ```

4. **Build Applications**
   ```
   "Build a working todo list web app"
   "Create a calculator webpage"
   ```

### Using Example Queries

Click any of the example query buttons in the sidebar to quickly test the agent's capabilities.

### Downloading Created Files

1. Files appear in the sidebar under "📁 Created Files"
2. Click on a file to preview its content
3. Use the download button to save files locally
4. For web apps, download all files and open `index.html` in your browser

## 🧠 How It Works

The AI Agent follows an autonomous loop powered by Claude Sonnet 4:

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
│  (Claude)   │       │
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
- **AI Model**: Claude (Anthropic)
- **APIs**: wttr.in (Weather data)
- **Language**: Python 3.12+

### Project Structure

```
ai-agent-assistant/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not in repo)
├── .gitignore         # Git ignore rules
├── LICENSE            # MIT License
└── README.md          # This file
```

### Available Tools

| Tool | Description | Input Format |
|------|-------------|--------------|
| `get_weather` | Fetches real-time weather data from wttr.in | City name (string) |
| `create_file` | Creates files with specified content | `filename\|content` |

## 💡 Example Queries

### Weather Information
```
"What's the weather in Paris?"
"How's the temperature in Mumbai?"
"Is it raining in Seattle?"
```

### Code Generation
```
"Write Python code to add two numbers"
"Create a function to reverse a string"
"Generate a sorting algorithm in JavaScript"
```

### Web Development
```
"Create a simple HTML page with a blue gradient background"
"Build a calculator webpage with modern design"
"Make a todo list app with HTML, CSS, and JavaScript"
"Design a landing page for a tech startup"
```

### File Creation
```
"Create a file called notes.txt with my shopping list"
"Generate a Python script for data processing"
"Make a markdown file with project documentation"
```

### Mathematics
```
"Solve this equation: 2x + 5 = 15"
"Calculate the derivative of x^2 + 3x"
"What's the area of a circle with radius 5?"
```

## 🛠️ Technologies Used

- **[Streamlit](https://streamlit.io/)** - Web framework for data apps
- **[Claude ](https://www.anthropic.com/claude)** - Advanced AI language model by Anthropic
- **[Python-dotenv](https://pypi.org/project/python-dotenv/)** - Environment variable management
- **[Requests](https://requests.readthedocs.io/)** - HTTP library for API calls

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `ANTHROPIC_API_KEY` | Your Claude API key from Anthropic | Yes |

### API Keys

Get your Claude API key:
1. Visit [Anthropic Console](https://console.anthropic.com/settings/keys)
2. Sign up or log in
3. Create a new API key
4. Add it to your `.env` file



## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions

- [ ] Add more tools (calculator, web scraper, database queries)
- [ ] Implement conversation memory across sessions
- [ ] Add support for image analysis
- [ ] Create comprehensive unit tests
- [ ] Improve error handling and logging
- [ ] Add voice input/output capabilities
- [ ] Implement rate limiting and caching
- [ ] Create a CLI version of the agent

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

**Sai Aneesh**
- GitHub: [@Saianeesh2003](https://github.com/Saianeesh2003)
- Email: gantisaianeesh@gmail.com
- Project Link: [https://github.com/Saianeesh2003/ai-agent-assistant](https://github.com/Saianeesh2003/ai-agent-assistant)
- Live Demo: [https://ai-agent-assistant-saianeesh.streamlit.app/](https://ai-agent-assistant-saianeesh.streamlit.app/)

## 🙏 Acknowledgments

- [Anthropic](https://www.anthropic.com/) for Claude Sonnet 4, the powerful AI model
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [wttr.in](https://wttr.in/) for free weather data API
- The open-source community for inspiration and support

## 🌟 Star History

If you found this project helpful, please consider giving it a ⭐!

---

<div align="center">

**Made with ❤️ by Sai Aneesh**


[Report Bug](https://github.com/Saianeesh2003/ai-agent-assistant/issues) · [Request Feature](https://github.com/Saianeesh2003/ai-agent-assistant/issues) · [View Demo](https://ai-agent-assistant-saianeesh.streamlit.app/)

</div>
