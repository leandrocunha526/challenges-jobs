# Usando uma imagem base com PHP e Apache
# Distribuição Linux: Debian
# PHP_ENV=production (ambiente)
FROM php:8.1-apache

# Instale extensões PHP necessárias
RUN docker-php-ext-install mysqli

# Copie todos os arquivos da pasta src para o diretório do Apache
COPY src/ /var/www/html/

# Defina o diretório de trabalho
WORKDIR /var/www/html

# Exponha a porta 80
EXPOSE 80

# Comando para iniciar o Apache
CMD ["apache2-foreground"]

