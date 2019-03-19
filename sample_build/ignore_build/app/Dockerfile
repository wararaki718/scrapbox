FROM ignore-base:1.0.0 as base

FROM python:3.6

WORKDIR /work
COPY --from=base /base/base.py /work/base.py
COPY src /work

CMD ["python", "app.py"]
