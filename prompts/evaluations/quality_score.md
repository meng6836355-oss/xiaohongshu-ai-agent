# Prompt Evaluation Framework

## Overview

This document defines the evaluation framework for Xiaohongshu AI Agent outputs.

The goal is to measure content quality consistently and improve agent performance over time.

Evaluation focuses on:

- Content quality
- User value
- Authenticity
- Engagement potential
- Platform compatibility

---

# Evaluation Pipeline

```
User Input

    ↓

Agent Generation

    ↓

Quality Evaluation

    ↓

Improvement Suggestions

    ↓

Optimization Agent

    ↓

Final Output
```

---

# Evaluation Dimensions

Each generated content item is scored from 0-100.

---

# 1. Hook Quality (20 points)

Measures whether the opening attracts user attention.

## Criteria

High score:

- Clear value proposition
- Strong curiosity
- Specific problem addressed
- Immediate relevance

Low score:

- Generic introduction
- Weak opening
- No clear benefit


Example:

Good:

```
I tested 20 AI tools for 30 days.
These 5 actually saved me hours.
```

Weak:

```
Today I want to share some AI tools.
```

---

# 2. Content Value (25 points)

Measures usefulness and information density.

## Criteria

Evaluate:

- Practical advice
- Actionable steps
- Real examples
- Unique insights


Questions:

- Can users learn something?
- Can users apply the information?

---

# 3. Authenticity (20 points)

Measures whether content feels human-created.

## Criteria:

High score:

- Personal perspective
- Specific experiences
- Natural language
- Balanced opinions


Low score:

- Generic AI wording
- Excessive marketing tone
- Unrealistic claims

---

# 4. Structure & Readability (15 points)

Measures content organization.

Evaluate:

- Clear sections
- Short paragraphs
- Logical flow
- Easy scanning


---

# 5. Platform Compatibility (10 points)

Measures Xiaohongshu suitability.

Evaluate:

- Community tone
- Appropriate hashtags
- Visual content potential
- User interaction potential


---

# 6. Safety & Compliance (10 points)

Measures policy compliance.

Check:

- No misinformation
- No harmful claims
- No copyright violations
- No privacy issues


---

# Scoring System

## 90-100 Excellent

Content is ready for publishing.

Characteristics:

- Strong hook
- High value
- Authentic voice
- High engagement potential


---

## 75-89 Good

Minor improvements recommended.

Possible improvements:

- Better title
- Stronger examples
- More emotional connection


---

## 60-74 Needs Improvement

Content requires optimization.

Issues:

- Weak structure
- Generic information
- Low differentiation


---

## Below 60

Requires regeneration.

Major problems:

- Poor relevance
- Low value
- Weak authenticity

---

# Evaluation Output Schema

Reviewer Agent should return:

```json
{
  "overall_score": 85,

  "scores": {
    "hook_quality": 18,
    "content_value": 22,
    "authenticity": 17,
    "readability": 14,
    "platform_fit": 8,
    "safety": 10
  },

  "strengths": [
    "Strong opening",
    "Clear examples"
  ],

  "weaknesses": [
    "Needs more personal perspective"
  ],

  "improvements": [
    "Add practical examples"
  ]
}
```

---

# Prompt Version Evaluation

Every prompt change should be evaluated.

Example:

```
writer_prompt_v1

vs

writer_prompt_v2
```

Compare:

| Metric | v1 | v2 |
|-|-|-|
| Hook Score | 75 | 88 |
| Value Score | 80 | 90 |
| Authenticity | 72 | 85 |
| Total | 76 | 87 |

---

# Future Automation

Planned:

- Automated evaluation pipeline
- LLM-as-Judge scoring
- Human feedback collection
- Prompt A/B testing
- Regression testing

---

# Vision

The evaluation framework allows Xiaohongshu AI Agent to continuously improve through measurable feedback instead of manual prompt adjustments.
