"""
Xiaohongshu AI Agent Backend

Main API entry point.
"""


def health_check():
    return {
        "status": "ok",
        "project": "xiaohongshu-ai-agent"
    }


if __name__ == "__main__":
    print(health_check())
