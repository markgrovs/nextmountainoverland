FROM python:3.11-alpine

RUN apk add --no-cache git openssh-client

WORKDIR /app

RUN pip install --no-cache-dir Pillow

COPY publisher.py /app/publisher.py
RUN chmod +x /app/publisher.py

CMD ["python", "-u", "/app/publisher.py"]
