FROM python:3.6-alpine
COPY entrypoint.sh /opt/
COPY cloud_test_app /opt/cloud_test_app
COPY etc/conf.py /etc/cloud_test/
RUN apk add --no-cache \
      bash \
      gcc \
      curl \
      g++ \
      libstdc++ \
      linux-headers \
      musl-dev \
      postgresql-dev \
      mariadb-dev;

RUN pip install gunicorn
RUN pip install -r /opt/cloud_test_app/requirements.txt

EXPOSE 8000
WORKDIR /opt
ENTRYPOINT ["/opt/entrypoint.sh"]
CMD ["--start-service"]
