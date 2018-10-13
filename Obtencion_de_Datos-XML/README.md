### Práctica Obtención de Datos

El objetivo de la práctica es la generación de un dataset en formato RDF/XML sobre el transporte público en Londres, a partir de la obtención de diversos datasets y de la integración de los mismos.


Instruccciones de ejecucion:

1.- Generar archivos StationFacilitiesNOH.xml y StepFreeTubeNNone.xml de apartados 2 y 3, para ello accedemos a los datasets de la API de datos abiertos de TfL

    $ python apartado_1_2_3.py

2.- Generar archivo TFLfacilities.xml de apartado 5, resultado de la integración de los dos ficheros anteriores:

    $ python apartado_5.py

3.- Generar archivo grafoRDF.xml de apartado 6 utilizando la librería rdflib:

    $ pytho apartado_6.py


Se incluye en la carpeta archivos_output el conjunto de archivos resultantes de la ejecución detallada previamente.

*Autores del proyecto: Candela Vidal, Remedios Blazquez y Jaime Zamorano*
