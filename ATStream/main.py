import streamlit as st
from llm import call_llm_service

st.title("LLM ATS Friendly CV & Cover Letter Generator")
st.markdown("This application generates a **ATS Friendly** **CV** and **Cover letter** based on a job description and resume data.")

st.sidebar.header("Input Resume Data")
job_title = st.text_area("Job Title: ")
job_description = st.text_area("Job Description: ")
work_experience = st.sidebar.text_area("Work Experience: ")
education = st.sidebar.text_area("Education: ")
skills = st.sidebar.text_area("Skills: ")
certifications = st.sidebar.text_area("Certifications: ")
projects = st.sidebar.text_area("Projects: ")

st.write(f"Job Title: {job_title}")

if st.button("Generate CV and Cover Letter"):
    if not job_title or not job_description or not work_experience:
        st.error("Please fill in all required fields.")
    else:
        prompt = f"""
        Role: You are an expert in generating ATS friendly CVs and cover letters.
        Task: Generate an ATS Friendly cover letter and CV based on the provided job description and resume data.
        Job Title: {job_title}
        Job Description: {job_description}
        Work Experience: {work_experience}
        Education: {education}
        Skills: {skills}
        Certifications: {certifications}
        Projects: {projects}
        """
        
        try:
            response = call_llm_service(prompt)
            st.success("Cover letter & CV generated successfully!")
            st.write(response)
        except Exception as e:
            st.error(f"Error generating cover letter: {e}")
