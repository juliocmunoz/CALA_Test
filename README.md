# CALA_Test
Prueba Técnica CALA - Análisis de Sentimientos / FASTAPI


Esta es la prueba técnica solicitada por CALA. El objetivo de esta prueba es obtener las reseñas de una app de la playstore para realizar un análisis de sentimientos de los comentarios de los usuarios. De esta forma, se puede obtener la connotación (**Positivo** o **Negativo**) de un comentario y se puede predecir la calificación que podría otenerse.

El archivo *main.py* cuenta con las funciones necesarias para obtener las reseñas. Para facilitar la implementación del código se alojaron las reseñas descargadas en un arcvhio **csv** alojado en *Google Drive*. Estas reseñas pueden ser consultadas [Aquí](https://drive.google.com/file/d/1sjUPK4jhkeKGhnOZO0DedakRP0NycP6F/view?usp=sharing). Sin embargo, se incluye una función para realizar el *scraping* de las reseñas y preparar el dataset para su análisis.

Como se solicitó, se implento una API simple mediante **fastAPI** para relaizar las pruebas de predicción del texto cómo para mostrar las **n** reseñasrequeridas por el usuario. La implementación se realizó en un ambiente virtual, por esto, se incluyen las dependencias necesarias en el archivo **requierements.txt**.


### Implementación fastAPI

Para la implementación en *fastAPI* se definieron los endpoints de la API, para este caso dos rutas, las cuales se listan a continuación:

- */get-predictions/texto_a_predecir=* : esta ruta usa la función *get_predictions*, la cual toma como argumento un texto ingresado por el usuario. El reusltado del análisis de ese texto es la connotación, ya sea positiva o negativa del comentario, y la posible calificación esperada con base en ese texto.
    
- */get-reviews/numero_de_reviews=* : esta ruta regresa los *n* comentarios más actuales, donde *n* es un número ingresado por el usuario para visualizar las reseñas. El contenido de esta reseñas fue simplificado para visualizar el contenido de la reseña, la connotación de la reseña y la fecha en la que se realizó.

El API se puede inicializar con la siguiente instrucción en la línea de comando, en la ubicación del archivo *main.py*.

```
uvicorn main:app --reload
```

Se puede acceder al API mediante la dirección de localhost ( http://127.0.0.1) en el puerto 8000.

```
http://127.0.0.1:8000
```
FastAPI incluye un dashboard para visaulizar estas rutas. Este dashboard se puede accesado mediante la dirección:

````
http://127.0.0.1:8000/docs
````
En este dashboard se muestran las rutas implementadas y una forma de interactuar con ellas.

### Modelo de análisis

El modelo de análisis fue implementado con *sklearn*. Se trata de un modelo simple que análisas la bolsa de palabras de la reseña y la relaciona con la calificación obtenida. De esta forma, se puede obtener un análisis sobre la connotación del texto y se puede predecir la calificación que s epodría obtener. El modelo arroja una precisión del **80%**, sin embargo esta predicción se puede mejorar. Además, podría ser comparada con otros modelos y otro tipo de métricas para obtener un mejor desmepeño.

### Despliege en Heroku

LA API implementada mediante *fastAPI* se desplegó en **Heroku**. De esta forma, se puede comprobar la funcionalidad sin la necesiad de realizar una instalación local. La aplicación se puede revisar en: https://calatestjcmb.herokuapp.com/ la página principal despliega un mensaje a modo de bienvenida.

De la misma forma que en su versión local, la app depslegada en **Heroku** permite tener acceso al dashboard para comprobar las rutas. 
````
https://calatestjcmb.herokuapp.com/docs
````
De esta forma, al ingresar al [dashboard](https://calatestjcmb.herokuapp.com/docs) se puede interactuar con los dos eventos.



