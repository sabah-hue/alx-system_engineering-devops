#Using Puppet, create a manifest that kills a process named killmenow
file { 'kill process':
    command  => 'pkill killmenow',
    provider => shell,
}
