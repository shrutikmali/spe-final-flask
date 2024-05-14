FROM python:3
COPY requirements.txt ./
COPY server.py ./
RUN apt update && apt install -y tesseract-ocr && apt install -y libtesseract-dev
RUN pip install --no-cache-dir -r requirements.txt
CMD flask --app server run
