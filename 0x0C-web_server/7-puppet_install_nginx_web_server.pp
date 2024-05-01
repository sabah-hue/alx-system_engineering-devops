# Using Puppet, configuring my server
exec { 'install_nginx':
    command  => 'sudo apt-get -y update;
    sudo apt-get -y install nginx;
    sudo chown -R "$USER":"$USER" /var/www/html/index.nginx-debian.html;
    sudo echo "Hello World!" > /var/www/html/index.nginx-debian.html;
    sudo sed -i "/server_name _;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-enabled/default;
    sudo service nginx restart',
    provider => shell,
}
