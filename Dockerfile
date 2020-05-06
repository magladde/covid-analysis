FROM python:latest
RUN pip install pandas && \
    pip install numpy && \
    pip install matplotlib
COPY . /tmp/
