FROM python:3.8

WORKDIR /aliyo

ENV PYTHONUNBUFFERED=1
ENV PORT=8000

ADD . /aliyo

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /aliyo

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD gunicorn aliyo.wsgi:application --bind 0.0.0.0:$PORT