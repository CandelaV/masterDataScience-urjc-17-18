### Práctica Bases de Datos No Convencionales.

El objetivo de la práctica es la captura, procesamiento, almacenamiento y
análisis de datos de la base de datos DBPL Computer Science Bibliography utilizando
MongoDB y Neo4j.

La recopilación completa de datos se descarga como un único fichero XML desde http://dblp.uni-trier.de/xml/

#### Preprocesamiento con pySpark
**Procesamiento_SparkSQL.ipynb**

Procesamiento del XML descargado para convertirlo a formato JSON, pudiéndose descartar aquellos elementos que se consideren irrelevantes. Para ello se construye un programa en python y se hace uso de Spark por el gran tamaño de los datos de entrada.

#### MongoDB
**Consultas_MongoDB**

Tras preprocesar los datos, se almacenan en una base de datos MongoDB realizando un adecuado diseño de la misma y se realizan una serie de consultas utilizando el lenguaje de consulta propio de la Base de Datos.

#### Neo4j
**Consultas_Neo4j**

Al igual que con MongoDB, se almacenan los datos despues de haberlos procesado adecuadamente con pySpark y se realizan sobre ellos tres consultas adecuadas a una base de datos orientada a grafos.

*Autoras del proyecto: Candela Vidal, Remedios Blazquez y Leda Duelo*
