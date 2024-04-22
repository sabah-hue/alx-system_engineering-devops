# SSH configuration file for the local SSH client
file { 'ssh_config':
    ensure  => 'file',
    path    => '~/etc/ssh/school',
    content => 'Host *
                      IdentityFile ~/.ssh/school
                      PasswordAuthentication no',
}
