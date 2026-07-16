# Contributing to Xiaohongshu AI Agent

First of all, thank you for your interest in contributing to Xiaohongshu AI Agent!

We welcome contributions from developers, researchers, creators, and AI enthusiasts who want to improve open-source AI agent technology.

Every contribution helps make this project better.

---

## 🌟 Ways to Contribute

There are many ways you can contribute:

### 🐛 Report Bugs

Found a problem?

Please create an issue and include:

- A clear description of the problem
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment information

---

### 💡 Suggest Features

We welcome ideas for:

- New AI agent capabilities
- Better workflows
- Developer tools
- Performance improvements
- User experience improvements

Please open a feature request issue.

---

### 📝 Improve Documentation

Documentation improvements are highly valuable.

You can help by:

- Fixing typos
- Adding examples
- Improving tutorials
- Translating documentation

---

### 💻 Submit Code

You can contribute:

- New agents
- Plugins
- Tools
- Bug fixes
- Performance optimizations

---

# Development Setup

## Requirements

Recommended environment:

- Python >= 3.10
- Git
- OpenAI API Key


## Clone Repository

```bash
git clone https://github.com/meng6836355-oss/xiaohongshu-ai-agent.git

cd xiaohongshu-ai-agent
```


## Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```


## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Project Structure

```
xiaohongshu-ai-agent/

├── src/
├── tests/
├── examples/
├── docs/
├── README.md
└── CONTRIBUTING.md
```

---

# Code Style

Please follow:

- PEP 8
- Clear variable names
- Type hints when possible
- Small and focused functions
- Meaningful comments

Example:

```python
def generate_post(topic: str) -> str:
    """
    Generate Xiaohongshu content from topic.
    """
    pass
```

---

# Testing

Before submitting a Pull Request:

Run tests:

```bash
pytest
```

Make sure:

- All tests pass
- No existing functionality breaks

---

# Pull Request Process

## 1. Fork Repository

Create your own fork.

## 2. Create Branch

Use descriptive branch names:

Feature:

```
feature/add-image-agent
```

Bug fix:

```
fix/api-timeout
```

Documentation:

```
docs/update-readme
```


## 3. Commit Changes

Write meaningful commit messages:

Good:

```
Add keyword analysis agent
```

Avoid:

```
update
fix stuff
changes
```

---

## 4. Submit Pull Request

Your PR should include:

- Description of changes
- Why this change is needed
- Testing information
- Screenshots/examples if applicable

---

# Issue Guidelines

Before creating an issue:

- Search existing issues
- Confirm the problem is reproducible
- Provide enough context


---

# Community Guidelines

We expect all contributors to:

- Be respectful
- Welcome different opinions
- Focus on constructive discussion
- Help other contributors

---

# License

By contributing to Xiaohongshu AI Agent, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping build an open-source AI Agent ecosystem! 🚀
