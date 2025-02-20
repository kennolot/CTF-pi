FROM python:3.13-slim

WORKDIR .

COPY app/app.py .

COPY answers/flag.txt flag.txt

RUN chmod 600 flag.txt

RUN apt-get update && apt-get install -y iputils-ping
RUN pip install flask

EXPOSE 8080

CMD ["python", "app.py"]
