# dog_python

Dentro la carpeta env (creada con virtualenv), se encuentra el codigo dog.py

El entorno virtualenv nos facilita el setup inicial del entorno para ejecutar python3.

Hay que instalarlo con pip (el gestor de plugins para python), 

$ sudo pip install virtualenv


Para ejecutar el entorno Python3:

$ virtualenv env --python=python3

Lo ejecutamos con el comando:

$ cd env
$ source bin/activate
(env)$ python dog.py


Para desactivar el entorno virtualenv hacemos:

(env)$ deactivate
$
