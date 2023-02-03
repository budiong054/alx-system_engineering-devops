# This puppet manifest configure Nginx server

exec {'Config Ubuntu Machine':
  command  => 'sudo apt-get update;
		sudo apt-get install nginx -y;
		echo "Hello World!" | sudo tee index.html;
		new_config="\ \n\tlocation \/redirect_me \{\ \n\t\treturn 301 \$scheme\:\/\/\$http_host\;\ \n\t\}\ \n";
		sudo sed -i "/server_name _;/a $new_config" /etc/nginx/sites-enabled/default',

  provider => shell,
}
