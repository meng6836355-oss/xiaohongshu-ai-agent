# Prompt System

The `prompts` directory contains the intelligence layer of Xiaohongshu AI Agent.

Each AI agent is powered by carefully designed prompts that define:

- Role
- Goals
- Reasoning workflow
- Input format
- Output format
- Constraints
- Evaluation criteria

---

# Agent Architecture

```
User Request

      |
      ▼

Planner Agent
      |
      ▼

Research Agent
      |
      ▼

Writer Agent
      |
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

# Available Agents

| Agent | Responsibility |
|---|---|
| Planner | Content strategy and planning |
| Researcher | Topic and trend analysis |
| Writer | Content generation |
| Reviewer | Quality evaluation |
| Optimizer | Engagement optimization |

---

# Prompt Design Principles

## Clear Role

Every agent has a specific responsibility.

## Structured Output

Agents should return predictable formats.

## Self Evaluation

Agents should review their own output.

## Extensibility

New agents can be added without changing the whole system.

---

# Future Improvements

Planned:

- Prompt version management
- Automatic evaluation
- A/B testing
- Prompt marketplace
- Community contributed agents
