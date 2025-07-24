import streamlit as st
from llm import call_llm_service

st.title("LLM ATS Friendly CV & Cover Letter Generator")
st.markdown("This application generates a **ATS Friendly** **CV** and **Cover letter** based on a job description and resume data.")

st.sidebar.header("Input Resume Data")
job_title = st.text_area("Job Title: ")
company_name = st.text_area("Company Name: ")
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
        Role: You are an expert ATS (Applicant Tracking System) specialist and a professional career coach. Your primary goal is to maximize the candidate's chances of passing through ATS screening and impressing hiring managers.

        Task: Generate a highly ATS-friendly and compelling Cover Letter and Resume tailored specifically to the provided job description and the candidate's personal data. Focus on keyword optimization, action verbs, quantifiable achievements, and a clean, readable format.
        
        Input Data (User Provided):
        Job Title: {job_title}
        Company Name (for Cover Letter): {company_name}
        Job Description: {job_description}
        Candidate Work Experience: {work_experience}
        Format: List each role with [Job Title], [Company Name], [Location] (Start Date – End Date).
        Description: For each role, provide bullet points detailing responsibilities and achievements. Quantify achievements whenever possible.
        Candidate Education: {education}
        Format: List each degree/certification with [Degree/Certification]. [Major/Field], [Institution Name], (Graduation Date/Completion Date)
        Candidate Skills: {skills}
        Format: Provide a comma-separated list of technical skills, soft skills, and tools (categorize skills).
        Candidate Certifications: {certifications}
        Format: List each certification with [Certification Name], (Issuing Body).
        Candidate Projects: {projects}

        Output Structure & Requirements:
        Provide the output in two distinct sections: Cover Letter and Resume, both formatted using Markdown for clarity and easy parsing.
        1. Cover Letter:
        Important Guidelines: Do not add or make up any skills, expriences, or qualifications that are not provided by the user. The cover letter and resume should be concise, professional, and tailored to the job description.
        Length: Approximately 3-4 paragraphs (max 1 page).
        Tone: Professional, enthusiastic, confident, and concise.
        Content:
        Paragraph 1 (Introduction): State the position you're applying for, where you saw the advertisement, and a brief, compelling statement about why you are a strong fit.
        Paragraph 2-3 (Body): Highlight 2-3 key experiences, skills, or achievements that directly align with the job description. Use strong action verbs and quantify results. Directly reference keywords from the job description. Explain how your skills benefit the company.
        Paragraph 4 (Conclusion): Reiterate your interest, express eagerness for an interview, and thank the reader for their time and consideration.
        
        2. Resume:
        Important Guidelines: Do not add or make up any skills, expriences, or qualifications that are not provided by the user. The cover letter and resume should be concise, professional, and tailored to the job description.
        Length: Maximum 2 pages. Prioritize relevance and impact.
        ATS Optimization:
        Keywords: Integrate relevant keywords from the job description naturally throughout the experience, skills, and project sections.
        Action Verbs: Start bullet points with strong action verbs (e.g., "Developed," "Managed," "Implemented," "Optimized," "Led").
        Quantification: Whenever possible, quantify achievements with numbers, percentages, or metrics (e.g., "increased efficiency by 20%," "managed a budget of $500K," "reduced errors by 10%").
        Formatting: Use a clean, standard, and easy-to-parse format. Avoid complex graphics, tables, or excessive columns that might confuse ATS.

        Sections:
        #### **Summary/Objective**
        #### **Work Experience**
        #### **Skills**
        Format: List all relevent skills user provided
        Example:
        - Category 1: Skill A, Skill B, Skill C
        - Category 2: Skill D, Skill E
        #### **Education**
        #### **Projects**
        #### **Certifications**

        Ensure the output is ATS-friendly, concise, and tailored to the job description provided. The goal is to create a compelling narrative that highlights the candidate's qualifications and makes them stand out to both ATS and hiring managers.
        """
        
        try:
            response = call_llm_service(prompt)
            st.success("Cover letter & CV generated successfully!")
            st.write(response)
        except Exception as e:
            st.error(f"Error generating cover letter: {e}")

if st.button("ATS & Interview Likelihood Assessment"):
    if not job_title or not job_description or not work_experience:
        st.error("Please fill in all required fields.")
    else:
        prompt_ass = f"""
        Input for Assessment: The generated Cover Letter, the generated Resume, the original Job Description, and the Candidate's original Input Data (Work Experience, Education, Skills, etc.).

        Task: Analyze the Job Description ({job_description}) and Candidate's Input Data {[work_experience, education, skills, certifications, projects]} to assess ATS compatibility and interview likelihood.

        Output Format:
        ### ATS & Interview Likelihood Assessment
        **Overall ATS Score:** [Percentage, e.g., 85%]
        * **Explanation:** [Brief explanation of the score, highlighting key strengths in ATS optimization (e.g., keyword matching, formatting).]
        **Interview Likelihood:** [Low/Medium/High]
        * **Explanation:** [Brief explanation of why the candidate is likely/unlikely to get an interview, considering both ATS factors and the overall alignment with the job requirements and desired candidate profile.]
        **Strengths:**
        **Areas for Improvement:**
        """

        try:
            assessment_response = call_llm_service(prompt_ass)
            st.success("ATS & Interview Likelihood Assessment generated successfully!")
            st.write(assessment_response)
        except Exception as e:
            st.error(f"Error generating assessment: {e}")