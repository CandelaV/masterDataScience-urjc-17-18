### Práctica Arquitecturas en la Nube. Docker

El objetivo de esta parte consiste en empaquetar y distribuir una aplicación en
contenedores docker.

Una vez desarrollada la aplicación (creada para la asignatura de Sistemas Distribuidos I de análisis de sentimientos de twitter con Hadoop), se realizará una pequeña ampliación y
se empaquetará como contenedores docker. Los resultados del
análisis se deberán guardar en una base de datos relacional (se ha elegido MySQL).

Tras la implementación de la aplicación completa, se empaquetará en contenedores orquestados con un fichero dockercompose.

**mysql-app** &rarr; situados en el directorio db-app se ejecuta el comando:


    $ docker build -t mysql-app .


**tweetanalysis-app** &rarr; situados en el directorio tweetanalysis-app se ejecuta el comando:


    $ docker build -t tweetanalysis .


**docker-compose.yml** &rarr; se ejecuta el siguiente comando introduciendo los parámetros indicados (NOTA: TIME en segundos, ha de ser suficiente para obtener un numero elevado de twitts):


    $ docker-compose run -e TIME=XXX -e ACCESS_TOKEN_KEY=XXX -e ACCESS_TOKEN_SECRET=XXX -e CONSUMER_KEY=XXX -e CONSUMER_SECRET=XXX twittananalysis

Una vez levantados ambos servicios y ejecutada la aplicacion se puede acceder al resultado conectandose a una shell del contenedor partea_db_1 con el comando:


    $ docker exec -it partea_db_1 bash

Dentro del contenedor, ejecutar los comandos:

    $ mysql -u root -p

    $ Password : admin

    mysql> use resultados;

    mysql> select * from tweets;

*Autoras del proyecto: Candela Vidal y Remedios Blazquez*
