FROM python:3.13-slim

WORKDIR /app

COPY app/app.py .

COPY answers/flag.txt flag.txt

RUN chmod 400 flag.txt

RUN apt-get update && apt-get install -y iputils-ping
RUN pip install flask

EXPOSE 80

CMD ["python", "app.py"]
