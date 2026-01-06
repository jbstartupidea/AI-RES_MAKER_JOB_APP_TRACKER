async function generate() {
  const jd = document.getElementById("jd").value;
  const resumeText = document.getElementById("resumeText").value;
  const fileInput = document.getElementById("resumeFile");
  const experience = document.getElementById("experience").value;

  if (!jd.trim()) {
    alert("Job Description is required");
    return;
  }

  const formData = new FormData();
  formData.append("job_description", jd);
  formData.append("years_of_experience", experience);
  formData.append("resume_text", resumeText);

  if (fileInput.files.length > 0) {
    formData.append("resume_file", fileInput.files[0]);
  }

  const res = await fetch("/generate-resume", {
    method: "POST",
    body: formData
  });

  const data = await res.json();
  document.getElementById("output").textContent =
    JSON.stringify(data, null, 2);
}
