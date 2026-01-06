import json
import os
import sys
from groq import Groq

sys.stdout.reconfigure(encoding="utf-8")


def build_experience_reference():
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    with open("data/profile_intelligence.json", "r", encoding="utf-8") as f:
        profile = json.load(f)

    with open("prompts/experience_reference.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": json.dumps(profile)}
        ],
        temperature=0.1
    )

    output = response.choices[0].message.content.strip()
    data = json.loads(output)

    with open("data/experience_reference.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print("[OK] Step 3 completed: experience_reference.json created")


if __name__ == "__main__":
    build_experience_reference()
