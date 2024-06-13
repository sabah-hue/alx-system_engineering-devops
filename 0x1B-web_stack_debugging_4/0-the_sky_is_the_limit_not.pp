# bring ULIMIT higher
exec { 'higher-ulimit':
    command => '/usr/local/bin:/bin/sed -i "s/15/2000" /etc/default/nginx',
}

exec { 'restat-nginx':
    command => '/etc/init.d/nginx restart',
}
