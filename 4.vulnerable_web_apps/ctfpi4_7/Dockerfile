FROM python:3.13-slim

WORKDIR /app

COPY app/app.py .

RUN mkdir adminfolder_local

COPY answers/flag.txt adminfolder_local/flag.txt

RUN chmod 400 adminfolder_local/flag.txt

RUN pip install flask

EXPOSE 8080

CMD ["python", "app.py"]
