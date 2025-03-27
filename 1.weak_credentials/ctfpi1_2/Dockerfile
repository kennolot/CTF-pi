FROM python:3.13-slim

WORKDIR /app

COPY answers/flag.txt .

COPY app/generate_weak_pw.py .
COPY app/login.py .

RUN pip install Flask

CMD ["python", "login.py"]
