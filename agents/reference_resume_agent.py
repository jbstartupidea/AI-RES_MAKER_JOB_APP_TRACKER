import json
import os
import sys
from groq import Groq

sys.stdout.reconfigure(encoding="utf-8")


def write_reference_resume():
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    with open("data/projected_experience.json", "r", encoding="utf-8") as f:
        projected = json.load(f)

    with open("prompts/reference_resume.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": json.dumps(projected)}
        ],
        temperature=0.1
    )

    output = response.choices[0].message.content.strip()
    data = json.loads(output)

    with open("data/reference_resume.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print("[OK] Step 5 completed: reference_resume.json created")


if __name__ == "__main__":
    write_reference_resume()
