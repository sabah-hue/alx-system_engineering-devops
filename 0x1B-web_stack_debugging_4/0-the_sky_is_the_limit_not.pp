# bring ULIMIT higher
exec { 'higher-ulimit':
    command => 'sed -i "s/15/4096" /etc/default/nginx',
}

exec { 'restat-nginx':
    command => '/et/init.d/nginx restart',
}
