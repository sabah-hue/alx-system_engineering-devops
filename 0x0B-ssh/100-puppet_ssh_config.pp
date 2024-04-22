# SSH configuration file for the local SSH client
file { 'Config-file':
    ensure  => 'file',
    path    => '/etc/ssh/school',
    content => '    IdentityFile ~/.ssh/school
                    PasswordAuthentication no',
}
