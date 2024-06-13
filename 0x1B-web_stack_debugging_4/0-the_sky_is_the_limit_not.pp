# bring ULIMIT higher
exec { 'higher-ulimit':
    command => 'sed -i "s/15/2000" /etc/default/nginx',
    path    => '/usr/local/bin/:/bin/',
}

exec { 'restat-nginx':
    command => '/etc/init.d/nginx restart',
}
