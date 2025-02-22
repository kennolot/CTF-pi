FROM python:3.13-slim

WORKDIR .

COPY source/broadcast.py .

COPY answers/flag.txt .

RUN chmod 400 flag.txt

EXPOSE 1337

CMD ["python", "broadcast.py"]
