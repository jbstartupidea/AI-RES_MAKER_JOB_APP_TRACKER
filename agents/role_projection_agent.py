import json
import os
import sys
from groq import Groq

sys.stdout.reconfigure(encoding="utf-8")


def run_role_projection():
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    with open("data/experience_reference.json", "r", encoding="utf-8") as f:
        exp = json.load(f)

    with open("data/jd_intelligence.json", "r", encoding="utf-8") as f:
        jd = json.load(f)

    with open("prompts/role_projection.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()

    payload = {
        "experience": exp,
        "jd": jd
    }

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": json.dumps(payload)}
        ],
        temperature=0.1
    )

    output = response.choices[0].message.content.strip()
    data = json.loads(output)

    with open("data/projected_experience.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print("[OK] Step 4 completed: projected_experience.json created")


if __name__ == "__main__":
    run_role_projection()
