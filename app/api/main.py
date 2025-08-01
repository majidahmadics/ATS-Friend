import uvicorn
from fastapi import FastAPI, UploadFile, File, Form
import shutil

app = FastAPI(
    title="ATS Friend",
    description="LLM ATS Friendly CV & Cover Letter Generator and Resume ATS Score Checker"
)

@app.get("/")
async def root():
    return {"message": "Welcome to the ATS Friend API. Use the endpoints to generate ATS-friendly CVs and cover letters or check resume ATS scores."}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):
    try:
        with open(f"uploaded_{file.filename}.pdf", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"file": f"uploaded_{file.filename}.pdf", "message": "Resume uploaded successfully."}
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/enter_job_info")
async def enter_job_info(job_description: str = Form(...), resume_data: str = Form(...)):
    return {"job_description": job_description, "resume_data": resume_data}

@app.get("/generate_cv")
async def generate_cv():
    return {"message": "Generate ATS-friendly CV based on job description and resume data."}

@app.get("/generate_cover_letter")
async def generate_cover_letter():
    return {"message": "Generate ATS-friendly cover letter based on job description and resume data."}

@app.get("/check_resume_score")
async def check_resume_score():
    return {"message": "Check the ATS score of your resume."}