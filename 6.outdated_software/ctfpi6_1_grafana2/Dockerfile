FROM grafana/grafana:8.3.0

COPY answers/flag.txt /tmp/flag.txt

RUN mkdir -p /home/grafana/.ssh
RUN cat /tmp/flag.txt > /home/grafana/.ssh/id_rsa

USER grafana

CMD ["grafana-server", "--homepath", "/usr/share/grafana"]
