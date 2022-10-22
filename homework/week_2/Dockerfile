FROM python:3.9-slim

COPY requirements.txt /app/
WORKDIR /app

RUN pip install --upgrade pip \
    &&  pip install --requirement requirements.txt

COPY plot.py .

CMD ["python", "plot.py"]