# ATS-Friend

## Overview

ATS-Friend is a web application designed to help job seekers create highly ATS (Applicant Tracking System)-friendly CVs and cover letters. It leverages the power of Large Language Models (LLMs) to generate tailored documents based on your job description and personal resume data, significantly increasing your chances of passing initial screenings and impressing hiring managers.

## Features

* **ATS-Friendly CV & Cover Letter Generation**: Generate professional and optimized CVs and cover letters specifically tailored to a given job description and your work experience, education, skills, and certifications.
* **Keyword Optimization**: The application focuses on integrating relevant keywords from the job description naturally throughout your resume and cover letter to maximize ATS compatibility.
* **Quantifiable Achievements**: Emphasizes the inclusion of quantifiable achievements (numbers, percentages, metrics) to showcase your impact effectively.
* **ATS & Interview Likelihood Assessment**: Get an assessment of your generated documents for ATS compatibility and overall interview likelihood, along with identified strengths and areas for improvement.

## Tech Stack

* **Python**: The core programming language used for the application.
* **Streamlit**: Used for building the interactive web user interface.
* **LLM (Groq)**: Powers the intelligent generation of CVs, cover letters, and assessments by utilizing the Groq API with the `llama-3.3-70b-versatile` model.
* **Heroku**: Deployment platform for the application.
* **Python-dotenv**: Manages environment variables for secure API key handling.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/majidahmadics/ats-friend.git](https://github.com/majidahmadics/ats-friend.git)
    cd ats-friend/ATS-Friend-5d2f96d8f6223b2f6aca285f1d4c3258f0aebdc9
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the `ATStream` directory (same level as `llm.py`) and add your Groq API key:
    ```
    GROQ_API_KEY="your_groq_api_key_here"
    ```
    You can obtain a Groq API key from the [Groq website](https://console.groq.com/docs/api-keys).

5.  **Run the application:**
    ```bash
    streamlit run ATStream/main.py
    ```

The application will open in your web browser.

## How to Use

1.  **Input Resume Data**: Fill in the text areas in the sidebar for "Work Experience", "Education", "Skills", "Certifications", and "Projects".
2.  **Enter Job Details**: Provide the "Job Title", "Company Name", and "Job Description" in the main input areas.
3.  **Generate CV and Cover Letter**: Click the "Generate CV and Cover Letter" button to receive a tailored CV and cover letter based on your inputs.
4.  **Get Assessment**: Click the "ATS & Interview Likelihood Assessment" button to receive an analysis of your generated documents.

## Contributing

Contributions are welcome! Please feel ATS-Friend to open issues or submit pull requests.