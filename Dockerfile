FROM python:3
COPY requirements.txt ./
COPY server.py ./
RUN pip install --no-cache-dir -r requirements.txt