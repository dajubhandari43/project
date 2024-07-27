import streamlit as st
import pickle
import pandas as pd

movies_dict=pickle.load(open('movie.pkl','rb'))
movie=pd.DataFrame(movies_dict)


similarity=pickle.load(open('similarity.pkl','rb'))



def recommend(movies):
  movie_index=movie[movie['title']== movies].index[0]
  distances=similarity[movie_index]
  movie_list=sorted(list(enumerate(distances)),reverse=True,key = lambda x:x[1])[1:6]


  recommended_movies=[]
  for i in movie_list:
    movies_id= i[0]
    recommended_movies.append(movie.iloc[i[0]].title)
  return recommended_movies  







st.title('Movie Recommendor System')

selected_movie_name= st.selectbox('Select the movie of your choise',movie['title'].values)


if st.button("Recommend"):
   recomendation= recommend(selected_movie_name)
   for i in recomendation:
     st.write(i)











