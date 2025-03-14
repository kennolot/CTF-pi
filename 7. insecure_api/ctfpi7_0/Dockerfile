FROM homeassistant/home-assistant:2023.1.0@sha256:13a84cb3cb0eaf66694f37e643706c4e23818f92beaeb08f0a9d587db63eb659

COPY answers/flag.txt /tmp/flag.txt


EXPOSE 8123

RUN adduser -D -s /bin/bash myuser

USER myuser

CMD ["python", "-m", "homeassistant"]
