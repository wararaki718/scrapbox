FROM golang AS build-env
# build
RUN go get -u github.com/labstack/echo/...
COPY app /work
WORKDIR /work
# compile
RUN go build -o server server.go

FROM ubuntu:16.04
WORKDIR /app
COPY --from=build-env /work/server .
CMD ["./server"]
