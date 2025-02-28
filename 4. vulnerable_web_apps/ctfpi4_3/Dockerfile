FROM python:3.13-slim

WORKDIR /app

COPY app/app.py .

COPY answers/flag.txt flag.txt

RUN chmod 400 flag.txt

RUN pip install flask

EXPOSE 8080

CMD ["python", "app.py"]