### Práctica Sistemas Distribuidos de Procesamiento de Datos I. Hadoop

En esta práctica se abordará el problema de
implementar un programa de análisis de sentimientos que utilice datos de Twitter y trabaje
con ellos utilizando el algoritmo MapReduce.

#### Obtencion del archivo JSON de twitts.

En un terminal situado en la carpeta en la que se encuentre el .py se ejecuta el siguiente comando

	python twitterstream.py > archivo_twitts.json

Se espera el tiempo necesario hasta obtener el volumen de twitts buscado, momento en el cual se puede interrumpir la ejecucion con "ctr + c"


#### Aplicación map-reduce de analisis de sentimientos de los twitts.


##### Ejecución en local con pipes.

En la terminal, situarse en la carpeta que contiene los archivos .py de mapper y reducer, el input de archivo_twitts.json y diccionarios. Ejecutar el siguiente comando:

	cat archivo_twitts.json | python mapper_final.py | sort | python reducer_final.py

La salida se imprime por pantalla.

##### Ejecución en cloudera con hadoop-streaming.

En la terminal situarse donde se encuentre el archivo_twitts.json y subirlo a hdfs con el comando:

	hdfs dfs -put archivo_twitts.json

En la terminal, situarse en la carpeta que contien los archivos .py de mapper y reducer, y los diccionarios. Ejecutar el siguiente comando:

	yarn jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -files mapper_final.py,reducer_final.py,State.tsv,AFINN-111.txt -mapper mapper_final.py -reducer reducer_final.py -input hdfs:///user/cloudera/archivo_twitts.json -output salida

Asegurarse que la carpeta del output "salida" no existe ya en la ruta /user/cloudera/ de hdfs.

En algunos casos el comando anterior fallaba, por lo que era necesario modificarlo ligeramente y ejecutar el siguiente comando:

	yarn jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -files mapper_final.py,reducer_final.py,State.tsv,AFINN-111.txt -mapper "python mapper_final.py" -reducer "python reducer_final.py" -input hdfs:///user/cloudera/archivo_twitts.json -output salida

El resultado obtenido se guarda en archivos de la forma "part-\*" en la carpeta de hdfs "/user/cloudera/salida"


*Autoras del proyecto: Candela Vidal y Remedios Blazquez*
