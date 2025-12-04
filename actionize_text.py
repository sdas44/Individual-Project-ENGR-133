"""
Course Number: ENGR 13300
Semester: e.g. Fall 2025

Description:
    This code contains functions that text into actionable tasks for the to do list. This utilizes Hugging Face's Inferemce Model API.
    

Assignment Information:
    Assignment:     Individual Project
    Team ID:        LC05 Team 5
    Author:         Samarth Das
    Date:           12/3/2025

Contributors:
    Name, login@purdue [repeat for each]

    My contributor(s) helped me:
    [X] understand the assignment expectations without
        telling me how they will approach it.
    [X] understand different ways to think about a solution
        without helping me plan my solution.
    [X] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

import os
from huggingface_hub import InferenceClient

def actionize_text(text):
    """
    Converts text into actionable tasks using a language model. This ultimately returns a JSON string containing the tasks.
    """
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
    """  
    saves the json text to a proper json file. Takes in string containing json coode and the output path.
    """
    with open(output_path, "w") as f:
        f.write(json_text)
    print(f"Extracted tasks saved to {output_path}")
