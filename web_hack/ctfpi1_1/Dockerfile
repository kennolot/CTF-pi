FROM python:latest

WORKDIR .

COPY app/app.py .

RUN pip install flask

EXPOSE 8080

CMD ["python", "app.py"]
