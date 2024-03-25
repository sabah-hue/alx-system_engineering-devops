#Using Puppet, install flask from pip3
file { 'install flask':
    command  => 'pip3 install Flask==2.1.0',
}
