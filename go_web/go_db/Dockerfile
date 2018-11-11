FROM golang AS build-env
# build
RUN go get -u github.com/labstack/echo/...
RUN go get github.com/lib/pq
COPY app /work
WORKDIR /work
# compile
RUN go build -o server server.go

FROM ubuntu:16.04
WORKDIR /app
COPY --from=build-env /work/server .
CMD ["./server"]
