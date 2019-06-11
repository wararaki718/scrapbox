FROM continuumio/anaconda3:2019.03

RUN conda install numpy scipy
COPY test.py test.py

CMD ["python", "test.py"]
