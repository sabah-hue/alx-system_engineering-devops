# SSH configuration file for the local SSH client
file { 'config':
    ensure  => 'file',
    path    => '/etc/ssh/ssh_config',
    content => 'Host *   
                    IdentityFile ~/.ssh/school
                    PasswordAuthentication no',
}
