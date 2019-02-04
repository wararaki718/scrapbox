FROM gcc:4.9 as gcc-env
COPY app1 /work/app
WORKDIR /work/app
RUN gcc -o appc app.c


FROM golang:1.8 as go-env
COPY app2 /work/app
WORKDIR /work/app
RUN go build -o appgo app.go


FROM python:3.6

COPY --from=gcc-env /work/app/appc /work/app/appc
COPY --from=go-env /work/app/appgo /work/app/appgo
COPY app3/app.py /work/app/app.py
COPY run.sh /work/run.sh

WORKDIR /work


CMD ["sh", "run.sh"]

