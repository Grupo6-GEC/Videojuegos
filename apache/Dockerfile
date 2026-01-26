FROM httpd:2.4

# Copiar las páginas y archivos desde la carpeta static de la API
COPY api/web/static/ /usr/local/apache2/htdocs/

# Copiar configuración de Apache
COPY apache/000-default.conf /usr/local/apache2/conf/extra/httpd-vhosts.conf

# Habilitar mod_proxy y mod_proxy_http
RUN echo "LoadModule proxy_module modules/mod_proxy.so" >> /usr/local/apache2/conf/httpd.conf \
    && echo "LoadModule proxy_http_module modules/mod_proxy_http.so" >> /usr/local/apache2/conf/httpd.conf \
    && echo "Include conf/extra/httpd-vhosts.conf" >> /usr/local/apache2/conf/httpd.conf
