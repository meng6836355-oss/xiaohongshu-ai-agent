# Xiaohongshu AI Agent

<p align="center">
  <strong>An Open-Source AI Agent Framework for Xiaohongshu Content Creation and Marketing Automation.</strong>
</p>

<p align="center">
Build AI-powered workflows for content generation, keyword research, trend discovery, publishing assistance, and creator productivity using modern LLMs.
</p>

---

## ✨ Overview

Xiaohongshu AI Agent is an open-source framework that helps creators, marketers, and developers automate Xiaohongshu workflows with AI.

Instead of building isolated prompts, the framework provides intelligent agents capable of planning, generating, reviewing, and optimizing content using large language models.

Whether you're an individual creator or a business managing multiple accounts, Xiaohongshu AI Agent provides a flexible foundation for AI-native marketing automation.

---

## 🚀 Features

- 🤖 AI-powered content generation
- 📝 Xiaohongshu note optimization
- 🔍 Keyword & hashtag research
- 📈 Trend discovery
- 💬 Comment summarization & analysis
- 🎯 Marketing strategy planning
- 🧠 Multi-Agent collaboration
- 🔌 Extensible plugin architecture
- ⚡ OpenAI API integration
- 🌍 Local deployment support
- 📦 Docker-ready
- 🔧 Developer-friendly APIs

---

## 🏗 Architecture

```text
                    User
                      │
                      ▼
              Xiaohongshu Agent
                      │
      ┌───────────────┼───────────────┐
      │               │               │
      ▼               ▼               ▼
 Planner Agent   Writer Agent   Review Agent
      │               │               │
      └───────────────┼───────────────┘
                      ▼
               OpenAI Models
                      │
                      ▼
             Xiaohongshu Workflow
```

The framework separates planning, generation, and review into independent agents, making it easier to extend and customize workflows.

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/meng6836355-oss/xiaohongshu-ai-agent.git

cd xiaohongshu-ai-agent
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

Create a `.env` file.

```env
OPENAI_API_KEY=your_api_key
```

### Run

```bash
python main.py
```

---

## 💡 Example

Input

> Generate a Xiaohongshu post introducing ChatGPT for productivity.

Output

```text
Title:
5 AI Tools That Save Me 3 Hours Every Day

Content:
I've been testing AI tools for several months...
...
```

---

## 🛣 Roadmap

- [x] Content Generation
- [x] Prompt Templates
- [ ] Trend Analysis
- [ ] Multi-Agent Workflow
- [ ] Browser Automation
- [ ] Memory System
- [ ] Knowledge Base (RAG)
- [ ] MCP Support
- [ ] Function Calling
- [ ] Workflow Engine
- [ ] Agent Marketplace

---

## 🧩 Tech Stack

- Python
- OpenAI API
- GPT Models
- FastAPI
- Docker
- SQLite / PostgreSQL
- LangGraph (planned)
- MCP (planned)

---

## 📚 Documentation

Documentation is currently under development.

Upcoming guides include:

- Quick Start
- Architecture
- Prompt Design
- Plugin Development
- Deployment
- API Reference

---

## 🤝 Contributing

We welcome contributions from the community.

You can help by

- Reporting bugs
- Suggesting new features
- Improving documentation
- Creating plugins
- Submitting Pull Requests

Please read **CONTRIBUTING.md** before contributing.

---

## 🌟 Vision

Our goal is to build the most powerful open-source AI Agent ecosystem for Xiaohongshu creators.

We believe AI should automate repetitive marketing tasks while allowing creators to focus on creativity.

---

## ❤️ Community

If this project helps you, please consider

⭐ Star this repository

🐛 Submit issues

💡 Share ideas

🚀 Contribute code

Every contribution helps the project grow.

---

## 📄 License

Released under the MIT License.

See the LICENSE file for details.
