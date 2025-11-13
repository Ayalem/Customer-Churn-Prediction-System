FROM python:3.12.5-slim


WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py  /app/
COPY  models/best_model.pkl  /app/models/


EXPOSE 9696

ENTRYPOINT [ "gunicorn","--bind=0.0.0.0:9696","app:app" ]


