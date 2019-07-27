FROM python:3.7
RUN apt-get update
COPY .  /
RUN apt-get -y install nginx
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
COPY proxy.conf /etc/nginx/conf.d/proxy.conf
#CMD python manage.py runserver 0.0.0.0:8000
RUN chmod +x entry.sh
CMD sh entry.sh