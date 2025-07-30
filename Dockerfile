FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "ATStream/main.py", "--server.port=8501", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]