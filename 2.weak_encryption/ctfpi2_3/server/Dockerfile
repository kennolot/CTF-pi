FROM python:3.13-slim

COPY server/app.py .
COPY answers/flag.txt /tmp/flag.txt

RUN pip install flask

EXPOSE 8000
CMD ["python", "app.py"]
