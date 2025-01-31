FROM php:7.4-apache
WORKDIR /var/www/html
COPY index.php .
COPY ./answers/flag.txt /flag.txt
RUN chmod 400 /flag.txt && chown root:www-data /flag.txt
EXPOSE 80
CMD ["apache2-foreground"]
