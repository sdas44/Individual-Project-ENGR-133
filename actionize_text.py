import os
from huggingface_hub import InferenceClient

def actionize_text(text):
    client = InferenceClient()

    prompt = f"""
You are a task extraction engine. 
Extract ALL actionable tasks from the following text.

Follow this exact JSON SCHEMA:

{{
    "tasks": [
        {{
            "id": "string",
            "name": "string",
            "description": "string",
            "due_date": "YYYY-MM-DD or null"
        }}
    ]
}}

Rules:
- Output ONLY valid JSON.
- Do not include explanations or extra text.
- Never include backticks.
- Generate a unique short id for each task (e.g., "task_1", "task_2", or any simple slug).
- For due_date: 
    - Convert "today", "tomorrow", etc. into YYYY-MM-DD.
    - If no due date is implied, use null.

TEXT:
<<<{text}>>>
"""

    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
    )

    json_text = completion.choices[0].message.content
    print(json_text)
    return json_text

def text_to_actions_file(json_text, output_path="extracted_tasks.json"):
    with open(output_path, "w") as f:
        f.write(json_text)
    print(f"Extracted tasks saved to {output_path}")
