# Using Puppet, Configure Nginx
exec { 'install_nginx':
    command  => 'sudo apt-get -y update;
    sudo apt-get -y install nginx;
    sudo sed -i "/server_name _;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default;
    sudo service nginx restart',
    provider => shell,
}
