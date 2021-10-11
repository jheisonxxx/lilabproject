Prueba Técnica para Lilab con django rest framework y docker
===

Para correr el projecto
=========

- *clonar el proyecto*:

```
    git clone https://github.com/jheisonxxx/lilabproject
```
- *construir el contenedor*:

```
    docker-compose -f docker-compose.yml build
```

- *Con esto ya estaría todo listo, lanzamos up para levantar el servicio y ya tendríamos nuestro proyecto completamente listo.*:

```
    docker-compose up
```
- *Para ver si hay migraciones y crearlas*:

```
    docker-compose -f docker-compose.yml run --rm web python manage.py makemigrations
```

- *Para realizar las migraciones*:

```
    docker-compose -f docker-compose.yml run --rm web python manage.py migrate
```