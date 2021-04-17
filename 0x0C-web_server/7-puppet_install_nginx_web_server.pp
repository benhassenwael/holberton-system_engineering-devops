#install and configure an Nginx server

exec { 'apt update':
  command => '/usr/bin/apt update'
}

-> package { 'nginx':
  ensure   => 'latest',
  provider => 'apt',
}
-> file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Holberton School',
}
-> file { '/var/www/html/custom_404.html':
  ensure  => file,
  content => 'Ceci n\'est pas une page',
}
-> file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => 'server {
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By $HOSTNAME;
        root /var/www/html;
        index index.html;
        server_name _;
        location / {
                try_files $uri $uri/ =404;
        }

        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }

        error_page 404 /custom_404.html;
        location = /custom_404.html {
                internal;
        }
}',
}
~> service { 'nginx':
  ensure   => 'running',
}
