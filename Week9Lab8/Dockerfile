FROM python:3.11-slim

ENV PYTHONPATH="/app"

WORKDIR /app

COPY ./main.py .

COPY ./classes ./classes

COPY ./functions ./functions

CMD [ "python", "main.py" ]