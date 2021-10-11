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


Para probar el projecto
=========


Precargar datos(puede obviarlos si se desea crear clientes y solicitudes desde cero
=====

```
docker-compose -f docker-compose.yml run --rm web python manage.py loaddata db_solicitudes.json
```

CLIENTES
=====

- *Para crear clientes*: Metodo POST: http://localhost:8000/clients/, en el campo punctuation, 2 es bueno, 1 es regular, 0 es malo, el campo dni es unico;

```
    utilizar el siguiente json
    {
    "dni": "45513063",
    "name": "Jheison Joel Talavera Begazo",
    "punctuation": 2,
    "debt_sbs": "34.90"
    }
```

- *Para ver el listado de clientes*: Metodo GET: http://localhost:8000/clients/

- *Para ver un cliente por id*: Metodo GET: http://localhost:8000/clients/[id]/

- *Para actualizar los datos de un cliente*: Metodo PATCH: http://localhost:8000/clients/[id]/, en el campo punctuation, 2 es bueno, 1 es regular, 0 es malo

```
    utilizar el siguiente json
    {
    "name": "Jheison Joel Talavera Begazo",
    "punctuation": 2,
    "debt_sbs": 34.95
}
```
SOLICITUDES
=====

- *Para crear solicitudes*: Metodo POST: http://localhost:8000/solicitudes/, el campo credit_indicator va desde de 1(crédito a pérdida) a 10(crédito seguro), amount es el monto del prestamo

```
    utilizar el siguiente json
     {
        "credit_indicator": 7,
        "client": 5,
        "amount": "20000.000"
    }
```

- *Para ver el listado de solicitudes*: Metodo GET: http://localhost:8000/solicitudes/

- *Para ver una solicitud por id*: Metodo GET: http://localhost:8000/solicitudes/[id]/

- *Para aprobar una solicitud*: Metodo PATCH: http://localhost:8000/solicitudes/[id]/, se maneja estados, 0 es pendiente, 1 es aprovado, 2 desaprovado

```
    utilizar el siguiente json
    {
    "state": 1
    }
```

- *Para desaprovar una solicitud*: Metodo PATCH: http://localhost:8000/solicitudes/[id]/, se maneja estados, 0 es pendiente, 1 es aprovado, 2 desaprovado

```
    utilizar el siguiente json
    {
    "state": 2
    }
```

- *Para ver el listado de solicitudes por estado de pendiente*: Metodo GET: http://localhost:8000/solicitudes/?state=1
- *Para ver el listado de solicitudes por estado de desaprobado*: Metodo GET: http://localhost:8000/solicitudes/?state=2
- *Para ver el listado de solicitudes por estado de desaprobado*: Metodo GET: http://localhost:8000/solicitudes/?state=1
