import streamlit as st
from llm import call_llm_service


st.title("Simple Session Manager")

job_title = st.text_area("Job Title: ")

if st.button("Generate Job Description"):
    if not job_title:
        st.error("Please enter a job title.")
    else:
        prompt = f"""
        You are a hiring manager looking to create a job description for the following position: {job_title}
        Please provide a detailed job description including responsibilities, qualifications, and any other relevant information.
        """
        response = call_llm_service(prompt)
        if job_title not in st.session_state:
            st.session_state[job_title] = response

# use the job description from session state outside the if block
st.write(st.session_state[job_title])

if st.button("Generate Resume"):
    if job_title not in st.session_state:
        st.error("Please generate a job description first.")
    else:
        prompt = f"""
        Based on the job description {st.session_state[job_title]} for {job_title}, please create a resume that highlights relevant skills, experiences, and qualifications.
        Ensure the resume is tailored to the job description provided.
        """
        response = call_llm_service(prompt)
        st.write(response)