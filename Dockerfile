FROM python:3.13.2

WORKDIR /app

COPY requirements.txt requirements.txt
COPY app.py app.py
COPY cert.pem cert.pem
COPY key.pem key.pem

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
