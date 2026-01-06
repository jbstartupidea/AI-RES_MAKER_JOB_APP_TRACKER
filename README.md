**AI-RES_MAKER_JOB_APP_TRACKER**

An AI-powered resume generation and job application support platform that dynamically creates FAANG-level, ATS-optimized resumes aligned to any Job Description (JD), with optional resume upload or text input.

This project is designed to intelligently transform user experience (real or synthetic) into role-aligned, recruiter-ready resumes using multi-agent AI orchestration.

🚀 Key Features

🔍 JD Intelligence Parsing

Extracts role expectations, skills, seniority, and domain signals from any Job Description.

🧠 Profile Intelligence Engine

Interprets user background (resume or none) into system-level experience.

🎯 Role Projection & Alignment

Projects experience into the target role, even when the user lacks direct experience.

🏆 FAANG-Style Resume Intelligence

Uses FAANG hiring patterns (impact, ownership, metrics) — without templates or copyrighted resumes.

📄 ATS-Optimized Resume Generation

Ensures keyword density, structure, and parsing safety.

📤 Multiple Input Modes

Paste resume text

Upload resume file

JD-only (experience synthesized)

🌐 FastAPI Backend + Web UI

REST API with Swagger docs

Simple extensible UI (future ChatGPT-style UI planned)

🧠 FAANG Resume Intelligence (Important Design Note)

This project does NOT ship FAANG resumes as templates.

Instead, it embeds FAANG hiring intelligence into AI agents:

Impact-driven bullet points

Metrics-first storytelling

Ownership and scope escalation

Recruiter-scan friendly structure

This approach is:

✅ Legal

✅ Ethical

✅ Adaptive to any JD

✅ Higher quality than static templates

🏗️ **Architecture Overview**
User Input (JD / Resume / File)
        ↓
JD Intelligence Agent
        ↓
Profile Intelligence Agent
        ↓
Experience Reference Agent
        ↓
Role Projection Agent
        ↓
Reference Resume Agent (FAANG style)
        ↓
ATS Resume Agent
        ↓
Final Resume Output

📁 **Project Structure**
AI-RES_MAKER_JOB_APP_TRACKER/
│
├── agents/
│   ├── jd_intelligence_agent.py
│   ├── profile_intelligence_agent.py
│   ├── experience_reference_agent.py
│   ├── role_projection_agent.py
│   ├── reference_resume_agent.py
│   └── ats_resume_agent.py
│
├── prompts/
│   ├── jd_intelligence.txt
│   ├── profile_intelligence.txt
│   ├── experience_reference.txt
│   ├── role_projection.txt
│   ├── reference_resume_agent.txt
│   └── ats_resume_agent.txt
│
├── data/
│   ├── job_description.txt
│   ├── raw_resume.txt
│   ├── *.json (generated outputs)
│
├── ui/
│   ├── index.html
│   ├── app.js
│   └── styles.css
│
├── api.py
├── requirements.txt
└── README.md

🛠️ **Tech Stack**

Backend: Python, FastAPI

AI Model: Groq (LLaMA-3.x)

Frontend: HTML, CSS, JavaScript

API Docs: Swagger (/docs)

Orchestration: Multi-Agent Pipeline

Deployment Ready: Docker / Cloud friendly

⚙️ **Installation & Setup (Step-by-Step)**
1️⃣ Clone the Repository
git clone https://github.com/jbstartupidea/AI-RES_MAKER_JOB_APP_TRACKER.git
cd AI-RES_MAKER_JOB_APP_TRACKER

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt


If requirements.txt doesn’t exist yet, create it with:

fastapi
uvicorn
groq
pydantic
python-multipart

4️⃣ Set Environment Variable (Groq API Key)

Windows (PowerShell):

setx GROQ_API_KEY "your_groq_api_key_here"


Restart terminal after setting this.

5️⃣ Run Backend Server
uvicorn api:app --reload

6️⃣ Access Application

Health Check:
http://127.0.0.1:8000/

Swagger API Docs:
http://127.0.0.1:8000/docs

UI:
http://127.0.0.1:8000/ui

🔌 API Usage
POST /generate-resume

Form Data:

job_description (required)

years_of_experience (required)

resume_text (optional)

resume_file (optional)

Returns paths to:

profile_intelligence.json

reference_resume.json

ats_resume.json

🧩 Future Enhancements

ChatGPT-style conversational UI

Resume version history

Job application tracker

Cover letter generator

Recruiter feedback simulation

Cloud deployment (AWS / GCP / Render)

⚠️ Disclaimer

This tool does not guarantee job placement.
It assists users in presenting skills effectively and ethically.

👨‍💻 Author

jbstartupidea
AI-first product builder | Systems thinker | Automation enthusiast
