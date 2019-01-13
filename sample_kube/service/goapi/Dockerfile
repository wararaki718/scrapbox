FROM golang AS build-env
# build
RUN go get -u github.com/labstack/echo/...
ADD app /work
WORKDIR /work
# compile
RUN go build -o server api.go

FROM ubuntu:16.04
WORKDIR /app
COPY --from=build-env /work/server .
CMD ["./server"]
