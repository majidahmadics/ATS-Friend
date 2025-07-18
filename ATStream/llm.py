import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

try:
    def call_llm_service(prompt: str) -> str:
        """
        Calls the LLM service to generate a cover letter based on the provided prompt.
        """
        client = Groq(
        api_key=API_KEY,
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama-3.3-70b-versatile",
        )

        return chat_completion.choices[0].message.content
except Exception as e:
    print(f"Error calling LLM service: {e}")
    raise e