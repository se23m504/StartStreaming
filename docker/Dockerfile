FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app/data

COPY config.py /app/bin/
COPY generate.py /app/bin/

CMD ["python", "/app/bin/generate.py"]
