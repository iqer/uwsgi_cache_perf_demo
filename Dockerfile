FROM python:2.7.18

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./ /data/apps

WORKDIR /data/apps

# ENTRYPOINT ['/usr/local/bin/dinit']

# CMD ["uwsgi", "--module=app", "--callable=app", "--master", "--processes=2", "--threads=2", "--enable-threads", "--harakiri=10", "--harakiri-verbose", "--lazy-apps", "--post-buffering=8192", "--buffer-size=32768", "--pidfile=/home/app/run/app.pid", "--vacuum", "--socket=/home/app/run/app.sock", "--chmod-socket=664", "--py-tracebacker=/home/app/run/app.sock", "--die-on-term", "--no-orphans", "--log-master", "--logto=/data/logs/uwsgi/app/demo_uwsgi.log", "--pythonpath=/data/apps"]
CMD ["uwsgi", "uwsgi.ini"]  