import json
import os
import sys
from groq import Groq

sys.stdout.reconfigure(encoding="utf-8")


def run_jd_intelligence():
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    with open("data/job_description.txt", "r", encoding="utf-8") as f:
        jd_text = f.read()

    with open("prompts/jd_intelligence_agent.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": jd_text}
        ],
        temperature=0.1
    )

    output = response.choices[0].message.content.strip()
    data = json.loads(output)

    with open("data/jd_intelligence.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print("[OK] Step 2 completed: jd_intelligence.json created")


if __name__ == "__main__":
    run_jd_intelligence()
