from fastapi import FastAPI

import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

import pickle
import os.path


from google_play_scraper import app, Sort, reviews_all

def remove_puntuation(text):
  final = "".join(u for u in text if u not in ("?", ".", ";", ":", "!", '"'))
  return final

def obtener_reviews(url):
  s = url 
  result = re.search('id=(.*)&hl', s)
  applicacion = result.group(1)
  claro_reviews = reviews_all(
      applicacion,
      sleep_milliseconds = 0,
      lang='es',
      country='co',
      sort=Sort.NEWEST
      )
  df_reviews = pd.DataFrame(np.array(claro_reviews), columns=['review'])
  df_reviews = df_reviews.join(pd.DataFrame(df_reviews.pop('review').tolist()))
  return df_reviews

def preparar_reviews(df_reviews):
  df_reviews['content'] = df_reviews['content'].astype(str)
  df_reviews['content'] .str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
  df_reviews['content'] = df_reviews['content'].str.upper()
  df_reviews_content = pd.DataFrame(df_reviews, columns=['content', 'score'])
  df_analysis = df_reviews[df_reviews['score']!=3]
  df_analysis['sentiment_score'] = df_analysis['score'].apply(lambda rating: +1 if rating > 3 else -1)
  positive = df_analysis[df_analysis['sentiment_score'] == 1]
  negative = df_analysis[df_analysis['sentiment_score'] == -1]
  df_analysis['sentiment'] = df_analysis['sentiment_score'].replace({-1 : 'negative', 1: 'positive'})
  df_analysis = df_analysis.dropna(subset=['content'])
  df_analysis['content'] = df_analysis['content'].apply(remove_puntuation)
  dfNew = df_analysis[['content', 'score']]
  
  return df_analysis, dfNew

def split(data):
 index = data.index
 data['random_number'] = np.random.randn(len(index))
 train = data[data['random_number']<=0.8]
 test = data[data['random_number']>0.8]
 return train, test

def prepare_data():
 url='https://drive.google.com/file/d/1sjUPK4jhkeKGhnOZO0DedakRP0NycP6F/view?usp=sharing'
 file_id=url.split('/')[-2]
 dwn_url='https://drive.google.com/uc?id=' + file_id
 df = pd.read_csv(dwn_url)
 return df


pipe = Pipeline([('Logistic', LogisticRegression())])

app = FastAPI()

df_reviews = prepare_data()
# En caso de no tener los reviews, esta función obtiene los reviews.
#df_reviews = obtener_reviews('https://play.google.com/store/apps/details?id=com.clarocolombia.miclaro&hl=es_CO&gl=US&showAllReviews=true')
df_analysis, dfNew = preparar_reviews(df_reviews)


@app.get("/")
def root():
	return {"message": "Prueba de Conocimientos: Análisis de Sentimientos"}


@app.get("/get-reviews/numero_de_reviews={item_id}")
async def get_reviews(item_id:int):
 
 
 df_show = df_analysis[['content','sentiment', 'at']]
 iris = df_show.head(item_id)
 #js = iris.to_json(orient = 'index')
 js = iris.values.tolist()

 return js

@app.get("/get-predictions/texto_a_predecir={texto_to_predict}")
async def get_predictions(texto_to_predict:str):
 train, test = split(df_analysis)
 vectorizer = CountVectorizer(token_pattern=r'[a-zA-Z]+')
 train_matrix = vectorizer.fit_transform(train['content'])
 test_matrix = vectorizer.transform(test['content'])
 X_train = train_matrix
 X_test = test_matrix
 y_train = train['score']
 y_test = test['score']
 pipe.fit(X_train, y_train)
 text = texto_to_predict
 text = text.split(';')
 text = vectorizer.transform(text)
 score = pipe.predict(text)



 train_matrix = vectorizer.fit_transform(train['content'])
 test_matrix = vectorizer.transform(test['content'])
 X_train = train_matrix
 X_test = test_matrix
 y_train = train['sentiment_score']
 y_test = test['sentiment_score']
 pipe.fit(X_train, y_train)
 connotacion = pipe.predict(text)

 if connotacion == 1:
  text = "positivo"
 else:
  text = "negativo"

 resultado = (f"La connotación del comentario es {text} y la calificación esperada es {score}")
 #score = pipe.score(X_test, y_test)

 return {
 		"texto_to_predict": texto_to_predict,
 		"resultado": resultado 

 		}



