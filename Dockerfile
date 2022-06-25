FROM ubuntu

COPY input.data.csv /data/
COPY output.data.csv /data/

RUN ls /data