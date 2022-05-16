FROM adminer

USER root
COPY login-env-vars.php /var/www/html/plugins/
RUN chmod 644 /var/www/html/plugins/login-env-vars.php
USER adminer
