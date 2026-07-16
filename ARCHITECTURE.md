# Architecture

## Overview

Xiaohongshu AI Agent is an open-source multi-agent framework designed to automate social media content workflows using Large Language Models (LLMs).

The system separates complex content creation tasks into specialized AI agents.

Each agent has:

- A dedicated role
- Specific responsibilities
- Structured input/output formats
- Independent prompts
- Evaluation criteria

This architecture improves reliability, extensibility, and maintainability.

---

# System Architecture

```
                         User
                           |
                           |
                           ▼

                 Xiaohongshu AI Agent

                           |
                           ▼

                 Orchestration Layer

                           |
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼

 Planner Agent     Researcher Agent     Writer Agent

        │                  │                  │
        └──────────────────┼──────────────────┘

                           ▼

                   Reviewer Agent

                           |
                           ▼

                  Optimizer Agent

                           |
                           ▼

              Final Xiaohongshu Content
```

---

# Agent Components

## Planner Agent

### Responsibility

Transforms user ideas into content strategies.

### Tasks

- Understand user goals
- Identify target audience
- Define content angle
- Create writing strategy


---

## Researcher Agent

### Responsibility

Analyze topics and discover content opportunities.

### Tasks

- Audience research
- Pain point analysis
- Trend discovery
- Competitive content analysis


---

## Writer Agent

### Responsibility

Generate Xiaohongshu content.

### Tasks

- Create titles
- Write content
- Generate hooks
- Recommend hashtags
- Create image prompts


---

## Reviewer Agent

### Responsibility

Evaluate generated content quality.

### Evaluation Criteria

- Hook strength
- Information value
- Authenticity
- Readability
- Platform compatibility


---

## Optimizer Agent

### Responsibility

Improve content performance.

### Tasks

- Optimize titles
- Improve opening hooks
- Increase engagement potential
- Refine structure


---

# Prompt Architecture

The intelligence layer is separated from application code.

```
prompts/

├── system/
│
│   ├── base.md
│   └── safety.md
│
├── agents/
│
│   ├── planner.md
│   ├── researcher.md
│   ├── writer.md
│   ├── reviewer.md
│   └── optimizer.md
│
├── templates/
│
└── evaluations/
```

Benefits:

- Easy prompt iteration
- Clear agent ownership
- Community contribution friendly
- Versionable AI behavior

---

# Data Flow

## Step 1: User Input

Example:

```
Create a Xiaohongshu post about AI productivity tools.
```

---

## Step 2: Planning

Planner Agent creates:

```json
{
 "audience": "knowledge workers",
 "angle": "productivity improvement",
 "strategy": "experience sharing"
}
```

---

## Step 3: Research

Researcher Agent analyzes:

- Audience needs
- Content opportunities
- Trending topics


---

## Step 4: Generation

Writer Agent creates:

```json
{
 "title": "",
 "content": "",
 "hashtags": []
}
```

---

## Step 5: Evaluation

Reviewer Agent scores:

```
Quality Score: 85/100

Strengths:
- Strong hook
- Clear structure

Improvements:
- Add more examples
```

---

## Step 6: Optimization

Optimizer Agent improves the final output.

---

# OpenAI Integration

The system integrates with OpenAI models through a dedicated client layer.

Architecture:

```
Agent Layer

      |
      |

OpenAI Client

      |
      |

OpenAI API

      |
      |

LLM Models
```

The client layer provides:

- API management
- Model configuration
- Error handling
- Future multi-model support

---

# Backend Architecture

```
backend/

├── api.py

API endpoints


├── config.py

Configuration management


├── openai_client.py

LLM communication layer


├── main.py

Application entry point
```

---

# Future Architecture Improvements

## Multi-Agent Orchestration

Planned:

- Agent workflow engine
- Agent communication protocol
- Dynamic agent selection


## Memory System

Planned:

- User preference memory
- Content history
- Knowledge retrieval


## MCP Support

Planned:

- External tools
- Data connectors
- Agent tool ecosystem


## Evaluation Framework

Planned:

- Automated benchmarks
- Prompt testing
- Quality scoring


---

# Design Principles

## Modularity

Each agent should solve one specific problem.

## Extensibility

Developers can add new agents without modifying existing components.

## Transparency

Prompt behavior should be understandable and customizable.

## Community First

The architecture is designed for open-source collaboration.

---

# Vision

Xiaohongshu AI Agent aims to become an open-source AI agent platform for creator intelligence, enabling developers and creators to build powerful AI-driven workflows.
