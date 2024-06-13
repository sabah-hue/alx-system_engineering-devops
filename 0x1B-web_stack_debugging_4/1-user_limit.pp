#Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.

exec { 'add-user':
    command => 'sudo adduser holberton',
    path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
    onlyif  => 'id -u holberton >/dev/null 2>&1 ||! id -u holberton',
}
