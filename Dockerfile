FROM python:3.11-slim

WORKDIR /app

COPY ./Lab2/auditor.py .

CMD [ "python", "auditor.py" ]