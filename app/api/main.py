import uvicorn
import shutil
from fastapi import FastAPI, UploadFile, File, Form
from ..services.pdf_parser import PDFParser

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
    if not file.filename.lower().endswith(".pdf"):
        return {"error": "Invalid file type. Only PDF files are allowed."}
    
    try:
        extracted_text = PDFParser.extract_text_from_pdf(file.file)

        if extracted_text:
            return {"file": f"uploaded_{file.filename}.pdf", "message": "Resume uploaded successfully.",
                "extracted_text": extracted_text}
        else:
            return {"error": "Failed to extract text from the PDF file."}
    except Exception as e:
        return {"error": f"An error occurred while processing the file: {e}"}

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