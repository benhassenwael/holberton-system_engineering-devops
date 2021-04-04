# making changes to config file to allow ssh connection

file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => '    PasswordAuthentication no',
  match => '    PasswordAuthentication.*'
}

file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => '    IdentityFile ~/.ssh/holberton',
  match => '    IdentityFile.*'
}
