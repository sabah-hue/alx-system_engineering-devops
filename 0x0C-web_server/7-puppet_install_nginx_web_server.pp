# Using Puppet, configuring my server
exec { 'Nginx HTTP':
    provider => 'shell',
    command  => 'apt-get -y update && apt-get -y install nginx && ufw allow 'Nginx HTTP' && chown -R "$USER":"$USER" /var/www/html/index.nginx-debian.html && echo "Hello World!" > /var/www/html/index.nginx-debian.html && sudo sed -i "/server_name _;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-enabled/default && echo "Ceci n'est pas une page" > /var/www/html/custom_404.html && sed -i "/redirect_me/a\\\terror_page 404 /custom_404.html;" /etc/nginx/sites-enabled/default && service nginx restart',
}
