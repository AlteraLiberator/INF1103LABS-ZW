FROM python:3.11-slim

WORKDIR /app

COPY ./Lab3/auditor.py .

CMD [ "python", "auditor.py" ]