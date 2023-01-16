# This puppet manifest kills a process named 'killmenow'

exec {'killmenow':
  command => '/bin/pkill -f killmenow',
}
