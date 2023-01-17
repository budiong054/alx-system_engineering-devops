# This puppet manifest makes changes to our configuration file

file_line {'ssh_config':
  path  => '~/.ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '*IdentityFile ~/.ssh/id_rsa',
}

file_line {'ssh_config':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthenticaion no',
  match => '*PasswordAuthentication Yes',
}
