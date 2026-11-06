FROM python:3.11-slim

WORKDIR /app

COPY ./main.py .
COPY ./inventory.json .
COPY classes ./classes
COPY functions ./functions

CMD ["python", "main.py"]
