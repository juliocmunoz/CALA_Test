# CALA_Test
Prueba Técnica CALA - Análisis de Sentimientos / FASTAPI


Esta es la prueba técnica solicitada por CALA. El objetivo de esta prueba es obtener las reseñas de una app de la playstore para realizar un análisis de sentimientos de los comentarios de los usuarios. De esta forma, se puede obtener la connotación (**Positivo** o **Negativo**) de un comentario y se puede predecir la calificación que podría otenerse.

El archivo *main.py* cuenta con las funciones necesarias para obtener las reseñas. Para facilitar la implementación del código se alojaron las reseñas descargadas en un arcvhio **csv** alojado en *Google Drive*. Estas reseñas pueden ser consultadas [Aquí](https://drive.google.com/file/d/1sjUPK4jhkeKGhnOZO0DedakRP0NycP6F/view?usp=sharing). Sin embargo, se incluye una función para realizar el *scraping* de las reseñas y preparar el dataset para su análisis.

Como se solicitó, se implento una API simple mediante **fastAPI** para relaizar las pruebas de predicción del texto cómo para mostrar las **n** reseñasrequeridas por el usuario.


