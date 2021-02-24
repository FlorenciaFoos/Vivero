# vivero
Catálogo online para vivero. Hecho con 
Python
Django
HTML , CSS
PostgreSQL DB

Deploy en: https://viverotalloverde.herokuapp.com/

 

 
###Pasos para ejecutar el proyecto de manera local.

Descarga del proyecto a través de git clone o ZIP

Setear un entorno con virtualenv y pip

###Creacion de entorno virtual

$ python -m venv 'nombre del entorno'

$ virtual/scripts/activate

###Install requirements

pip install -r requirements.txt

###Hacer las migraciones correspondientes

$ cd projectname/

$ python manage.py migrate

###Start the development server

$ python manage.py runserver
