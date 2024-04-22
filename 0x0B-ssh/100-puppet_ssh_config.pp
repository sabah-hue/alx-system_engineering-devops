# SSH configuration file for the local SSH client
file { 'ssh_config':
    ensure  => 'file',
    path    => '~/etc/ssh/ssh_config',
    content => 'Host *
                      IdentityFile ~/.ssh/school
                      PasswordAuthentication no',
}
