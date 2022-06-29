server {
    listen ${LISTEN_PORT};

    location /static {
        alias /val/static;
    }

    location / {
        uswgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uswgi_params;
        client_max_body_size    10M;
        
    }
}