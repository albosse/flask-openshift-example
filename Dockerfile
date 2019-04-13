FROM python:3.7-alpine

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN mkdir -p /deploy/flaskex

# Deploy application
COPY gunicorn_config.py /deploy/gunicorn_config.py
COPY flaskex /deploy/flaskex
WORKDIR /deploy/flaskex

ENV PYTHONPATH=/deploy

EXPOSE 8080

CMD ["gunicorn", "--config", "/deploy/gunicorn_config.py", "app:app"]
