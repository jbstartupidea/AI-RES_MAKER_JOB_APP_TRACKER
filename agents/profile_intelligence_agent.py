import json
import os
from groq import Groq


def extract_json_block(text: str) -> dict:
    """
    Safely extract the FIRST valid JSON object from LLM output.
    This prevents crashes due to explanations, markdown, or extra text.
    """
    brace_count = 0
    start_index = None

    for i, ch in enumerate(text):
        if ch == "{":
            if brace_count == 0:
                start_index = i
            brace_count += 1
        elif ch == "}":
            brace_count -= 1
            if brace_count == 0 and start_index is not None:
                json_text = text[start_index : i + 1]
                return json.loads(json_text)

    raise ValueError("No valid JSON object found in model output")


def build_profile_intelligence():
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    # Load prompt
    with open("prompts/profile_intelligence.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "Generate profile intelligence JSON only"}
        ],
        temperature=0.1
    )

    raw_output = response.choices[0].message.content.strip()

    # ✅ SAFE JSON extraction
    data = extract_json_block(raw_output)

    # Ensure output directory
    os.makedirs("data", exist_ok=True)

    # Write JSON file ONLY (API relies on this)
    with open("data/profile_intelligence.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    # ASCII-only print (Windows safe)
    print("[OK] Step 1 completed: profile_intelligence.json created")


if __name__ == "__main__":
    build_profile_intelligence()
