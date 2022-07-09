FROM python:3.10-slim
# FROM python:3.10-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--port", "8001", "--host", "0.0.0.0"]