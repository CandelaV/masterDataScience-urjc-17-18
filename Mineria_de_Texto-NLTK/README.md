### Práctica Mineria de Texto y Recuperación de Información. NLTK

El objetivo es poner en práctica diferentes conceptos aprendidos durante el curso y relacionados con la Recuperación de Información y el procesamiento de texto con la librería NLTK de Python, aplicándolos a una tarea real concreta.

La tarea ,en este caso, consiste en agrupar de forma automática noticias en base al tema o evento que describen. Además, las noticias pertenecen a diferentes fuentes y en dos idiomas distintos.

No ha sido necesario, puesto que se proporcionaba de origen, los documentos .html obtenidos de diferentes fuentes de noticias online y un código fuente en Python con un ejemplo completo de procesamiento de las páginas web en formato txt y agrupamiento mediante un algoritmo de clustering aglomerativo.

En la práctica se ha llevado a cabo cambios sobre el código proporcionado con cierto criterio, con el fin de mejorar los resultados de agrupamiento.



**TextToHtml.py** &rarr; Lee los .html y los transforma a .txt. Es necesario indicar la carpeta en la que se encuentran los archivos originales.

**BasicNewsClusteringFinal.py** &rarr; Lee los .txt, realiza sobre ellos una serie de transformaciones y ejecuta el algoritmo de clustering para obtener la clasificación por temas. Es necesario indicar la carpeta en la que se encuentran los .txt y si se desea utilizar entidades nombradas (named_ent = True) o no (named_ent = False)


Se incluye una memoria que recoge los resultados de todas los experimentos realizados, así como una página de introducción y otra de conclusiones.

*Autoras del proyecto: Candela Vidal, Remedios Blazquez*
