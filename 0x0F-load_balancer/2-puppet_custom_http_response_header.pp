# This puppet manifest automate the task of creating a custom
# HTTP header response

exec {'custom http header response':
  command  => 'sudo apt-get update;
  	sudo apt-get -y install nginx;
  	sudo sed -i "/server_name _;/i \ \n\tadd_header X-Served-By $HOSTNAME;\ \n" /etc/nginx/sites-enabled/default;
	sudo service nginx restart',
  provider => shell,
}
