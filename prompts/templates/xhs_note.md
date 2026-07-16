# Xiaohongshu Note Template

## Purpose

Standard output format for Xiaohongshu content generation.

This template is used by the Writer Agent and Optimizer Agent.

---

# Content Structure

## Metadata

```json
{
  "topic": "",
  "target_audience": "",
  "content_type": "",
  "style": ""
}
```

---

# Output Format

```json
{
  "title": "",

  "hook": "",

  "content": "",

  "hashtags": [],

  "image_prompt": "",

  "call_to_action": ""
}
```

---

# Field Description


## title

The main title of the post.

Requirements:

- Clear
- Attractive
- Easy to understand
- Suitable for Xiaohongshu style


Recommended:

- 10-20 Chinese characters
- Avoid clickbait


---

## hook

The opening sentence.

Purpose:

Capture attention in the first few seconds.

Should include:

- User pain point
- Curiosity
- Clear benefit


---

## content

Main body.

Recommended structure:

```
Problem

↓

Personal insight

↓

Solution

↓

Practical steps

↓

Summary
```


---

## hashtags

Related tags.

Requirements:

- Relevant to topic
- Search friendly
- Avoid spam


Example:

```json
[
 "AI工具",
 "效率提升",
 "学习方法"
]
```

---

## image_prompt

Prompt for AI image generation.

Should describe:

- Visual style
- Main subject
- Composition
- Mood


Example:

```
Minimal modern workspace,
AI productivity concept,
warm lighting,
clean aesthetic
```

---

## call_to_action

Optional interaction guidance.

Examples:

- Ask users to comment
- Encourage sharing experience
- Invite discussion
