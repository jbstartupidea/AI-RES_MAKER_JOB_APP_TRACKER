from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import subprocess
import sys
import os

app = FastAPI(title="Resume Coach AI")

# -----------------------------
# CORS (safe for UI + future)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Serve UI as ROOT
# -----------------------------
app.mount("/", StaticFiles(directory="ui", html=True), name="ui")

# -----------------------------
# Helper: run agent safely
# -----------------------------
def run_agent(script_name: str):
    result = subprocess.run(
        [sys.executable, f"agents/{script_name}"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"\n--- Agent Failed: {script_name} ---\n"
            f"STDOUT:\n{result.stdout}\n\n"
            f"STDERR:\n{result.stderr}\n"
        )

# -----------------------------
# API Endpoint
# -----------------------------
@app.post("/generate-resume")
async def generate_resume(
    job_description: str = Form(...),
    years_of_experience: int = Form(...),
    resume_text: str = Form(""),
    resume_file: UploadFile | None = File(None)
):
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)

    # Save JD
    with open("data/job_description.txt", "w", encoding="utf-8") as f:
        f.write(job_description)

    # Save pasted resume (if provided)
    if resume_text.strip():
        with open("data/raw_resume.txt", "w", encoding="utf-8") as f:
            f.write(resume_text)

    # Save uploaded resume (if provided)
    if resume_file:
        contents = await resume_file.read()
        with open(f"data/{resume_file.filename}", "wb") as f:
            f.write(contents)

    # Run pipeline
    run_agent("profile_intelligence_agent.py")
    run_agent("experience_reference_agent.py")
    run_agent("role_projection_agent.py")
    run_agent("reference_resume_agent.py")
    run_agent("ats_resume_agent.py")

    return {
        "status": "success",
        "message": "Resume generated successfully",
        "outputs": {
            "profile": "data/profile_intelligence.json",
            "experience": "data/experience_reference.json",
            "projected": "data/projected_experience.json",
            "reference_resume": "data/reference_resume.json",
            "ats_resume": "data/ats_resume.json"
        }
    }
