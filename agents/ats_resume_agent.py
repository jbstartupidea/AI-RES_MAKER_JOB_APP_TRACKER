import json
import os
from groq import Groq


def extract_json_block(text: str) -> str:
    brace_count = 0
    start = None

    for i, ch in enumerate(text):
        if ch == "{":
            if brace_count == 0:
                start = i
            brace_count += 1
        elif ch == "}":
            brace_count -= 1
            if brace_count == 0 and start is not None:
                return text[start:i + 1]

    raise ValueError("No valid JSON object found in model output")


def generate_ats_resume():
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    # Load reference resume (Step 4)
    with open("data/reference_resume.json", "r", encoding="utf-8") as f:
        reference_resume = json.load(f)

    # Load ATS resume prompt
    with open("prompts/ats_resume_agent.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": json.dumps(reference_resume)}
        ],
        temperature=0.1
    )

    raw_output = response.choices[0].message.content.strip()

    # ✅ STRICT JSON EXTRACTION (THIS WAS MISSING)
    json_block = extract_json_block(raw_output)

    try:
        ats_resume = json.loads(json_block)
    except json.JSONDecodeError as e:
        raise ValueError(
            "Invalid JSON returned by ATS agent:\n\n" + json_block
        ) from e

    os.makedirs("data", exist_ok=True)
    with open("data/ats_resume.json", "w", encoding="utf-8") as f:
        json.dump(ats_resume, f, indent=2)

    print("[OK] Step 5 completed: ats_resume.json created")


if __name__ == "__main__":
    generate_ats_resume()
