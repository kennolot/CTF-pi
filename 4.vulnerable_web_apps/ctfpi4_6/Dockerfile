FROM python:3.13-slim

WORKDIR /app

COPY app/app.py .

RUN mkdir -p ./hidden/admin

COPY answers/flag.txt ./hidden/admin/flag.txt

RUN chmod 400 ./hidden/admin/flag.txt

RUN pip install flask

EXPOSE 8080

CMD ["python", "app.py"]
