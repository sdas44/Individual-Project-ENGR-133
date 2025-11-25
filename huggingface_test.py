import os
from huggingface_hub import InferenceClient

client = InferenceClient()

completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": """
You are a task extraction engine. 
Extract ALL actionable tasks from the following text.

Follow this exact JSON SCHEMA:

{
  "tasks": [
    {
      "id": "string",
      "name": "string",
      "description": "string",
      "due_date": "YYYY-MM-DD or null"
    }
  ]
}

Rules:
- Output ONLY valid JSON.
- Do not include explanations or extra text.
- Never include backticks.
- Generate a unique short id for each task (e.g., "task_1", "task_2", or any simple slug).
- For due_date: 
    - Convert "today", "tomorrow", etc. into YYYY-MM-DD.
    - If no due date is implied, use null.

TEXT:
<<<Today I have a few important tasks to get through, starting with organizing my schedule so I can stay on track and avoid falling behind. I need to review any assignments or projects that are due soon and make sure I set aside enough time to finish them. I want to catch up on messages and emails since staying on top of communication helps everything run smoothly. At some point, I should take a break to clear my mind, grab some food, and reset before jumping back into what's left on my To Do List. Overall, today is going to be about staying focused, managing my time well, and making steady progress on everything I need to get done.>>>
"""
        }
    ],
)

print(completion.choices[0].message.content)