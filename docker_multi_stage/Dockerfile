FROM gcc:4.9 AS builder

ADD app /work
WORKDIR /work
RUN gcc hello.c

FROM ubuntu:16.04
WORKDIR /app
COPY --from=builder /work/a.out .
ENTRYPOINT ["./a.out"]