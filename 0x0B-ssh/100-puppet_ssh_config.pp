#configuration file to can connect to a server without typing a password.
file { 'Config-file':
  ensure  => 'file',
  path    => '/etc/ssh/ssh_config',
  content => '  IdentityFile ~/.ssh/school
                PasswordAuthentication no',
}
