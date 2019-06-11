FROM continuumio/miniconda3:4.6.14

RUN conda install numpy scipy
COPY test.py test.py

CMD ["python", "test.py"]
