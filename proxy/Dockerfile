FROM nginxinc/nginx-unprivileged:1-alpine
LABEL maintainer="Am Gh"

COPY ./default.conf.tpl /etc/ngnix/default.conf.tpl
COPY ./uswgi_params /etc/ngnix/uswgi_params
COPY ./run.sh /run.sh

ENV LISTEN_PORT=8000
ENV APP_HOST=app
ENV APP_PORT=9000

USER root

RUN mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

USER nginx

CMD ["/run.sh"]
