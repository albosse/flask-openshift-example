FROM python:3.7-alpine

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Deploy application
COPY gunicorn_config.py gunicorn_config.py
COPY flaskex /flaskex
WORKDIR /flaskex

EXPOSE 8080

CMD ["gunicorn", "--config", "gunicorn_config.py", "wsgi:app"]
