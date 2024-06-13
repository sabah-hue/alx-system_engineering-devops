# bring ULIMIT higher
exec { 'higher-ulimit':
    command => '/usr/bin/env sed -i s/15/4096 /etc/default/nginx',
}

exec { 'restat-nginx':
    command => 'service nginx restart',
}
