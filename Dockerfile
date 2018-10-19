FROM jasmin_env

COPY docker_app.py /home/app/

COPY template /home/app/template

COPY entrypoint.sh /home

WORKDIR /home

RUN chmod +x /home/entrypoint.sh

ENTRYPOINT ["/home/entrypoint.sh"]



