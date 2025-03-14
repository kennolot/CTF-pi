FROM grafana/grafana:8.3.0@sha256:9c23e4902591502d8992597b9af76a99767ddbd3b90d93cc4859b223945f2607

COPY answers/flag.txt /tmp/flag.txt

RUN mkdir -p /home/grafana/.ssh
RUN cat /tmp/flag.txt > /home/grafana/.ssh/id_rsa

USER grafana

CMD ["grafana-server", "--homepath", "/usr/share/grafana"]
