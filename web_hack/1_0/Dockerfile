FROM php:7.4-apache
WORKDIR /var/www/html
COPY index.php .
COPY ./answers/flag.txt /flag.txt
RUN chown www-data:www-data /flag.txt && chmod 440 /flag.txt
EXPOSE 80
CMD ["apache2-foreground"]
