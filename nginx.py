uwsgi --http :8000 --wsgi-file my_file.py
uwsgi --http :8000 --module django_project.wsgi
uwsgi --socket blog.sock --module blog.wsgi --chmod-socked=666

############################ CLI

sudo /etc/init.d/nginx restart
nginx - t @ check config before reload
nginx - T # display configs
nginx -s reload # reload configs
# Location
/etc/nginx/nginx.conf # main file
/etc/nginx/conf.d/*.conf # configs

########################## Django
#add config for project on /etc/nginx/sites-available/blog.conf
# to start using add link
## sudo ln -s /etc/nginx/sites-available/blog.conf /etc/nginx/sites-enabled/

upstream django {
  server unix:///home/udoms/blog/blog.sock;
}

server{
  listen  80;
  server_name blog.com www.blog.com;
  charset utf_8;
  client_max_body_size 75M: #max download size
  location /media { # server media files
    alias /home/udoms/blog/media; # physical location on disk
  }
  location /static { #serve static files
    alias /home/udoms/blog/static; # physical location on disk
  }
  location / { # serve remaining requests on django itself
    uwsgi_pass django; # ref to upstream django
    include /home/udoms/blog/uwsgi_params; # create with contents of https://uwsgi-docs.readthedocs.io/en/latest/Nginx.html
  }

# in the project folder of blog/
touch blog_uwsgi.ini

[uwsgi]
# full path to Django project's root directory
chdir            = /home/udoms/microdomains/
# Django's wsgi file
module           = microdomains.wsgi
# full path to python virtual env
home             = /home/udoms/env/md
# enable uwsgi master process
master          = true
# maximum number of worker processes
processes       = 10
# the socket (use the full path to be safe
socket          = /home/udoms/microdomains/microdomains.sock
# socket permissions
chmod-socket    = 666
# clear environment on exit
vacuum          = true
# daemonize uwsgi and write messages into given log
daemonize       = /home/udoms/uwsgi-emperor.log

@@ this is to avoid doing uwsgi <long parameters list> and instead do $uwsgi --ini blog_uwsgi.ini

############################ Use cases
* Web Server
* Reverse Proxy
* Load Balancer
* Cache
* Firewall
* DDOS protection
* Api gateway
* K8s IC
* Sidecar Proxy


#Config context
- One Main Context
- One HTTP Context

Main          #[ nro workers/ linux username / PID / log file loc]
  **** Events #[Connection processing dirs}
  **** HTTP   # [How nginx handles http/https]
  |      ****** Server # [Defines virtual server: domain name / IP address / unix socket ]
  |      |         ******* Location # [How virtual server process http request: point a path / string matching ]
  |      ****** Upstream       # [ Group of backend servers: load balancing ]
  |
  **** Stream # {layer 3 and 4: TCP / UDP]

# Directives

Dir: statement that controls NGINX behavior
Block: group of directives in a context

Server { # BLOCK start
  listen 80; # DIRECTIVE listen
  root /usr/share/nginx/html; # DIRECTIVE root
} # BLOCK end
