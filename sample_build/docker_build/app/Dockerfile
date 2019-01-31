FROM test-base:latest as base

FROM python:3.6

COPY show.py /work/show.py
COPY --from=base /work/base.txt /work/base.txt

WORKDIR /work
CMD ["python", "show.py"]
