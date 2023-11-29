# GUnicorn(:8000) + Nginx (:80) = access to static files served by nginx
# GUnicorn: serves the app throught WCGI and forks it on multiple workers. Does load balancing at OS kernel level
# Nginx: gunicorn drops requests with IO Error if every worker is occupied, nginx manages a queue to avoid that.
#        gunicorn doesnt start working until the data stream is read (buffering), so it's easy to DDOS
#        gunicorn can't serve static files
#        nginx and apache have integrations with plugins to mitigate DDOS, gunicorn wasn't build taking security into consideration
# Threat vs worker: threats share memory inside the same worker, less memory than 9 worker config

# requirements.txt
Django
GUnicorn

#Dockerfile
FROM python:3.11

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./django-project-files /app

WORKDIR /app
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]

#entrypoint.sh
#!/bin/sh
python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn django_project.wsgi:application --bind 0.0.0.0:8000 # numb of workers = 2*cpu + 1



#nginx config

upstream server_django{
  server 0.0.0.0:8000;
}

server{
  listen 80;
  location / {
    proxy_pass http://server_django;
    proxy_set_header X_Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Host $host;
    proxy_redirect off;
  }

  location /static/ {
    alias /app/static/;
  }
}
