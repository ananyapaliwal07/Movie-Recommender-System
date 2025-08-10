import streamlit as st
import pickle
import pandas as pd
import time
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
def recommend(movie):
    index = movies[movies['title']==movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommend_movies = [movies.iloc[i[0]].title for i in movie_list]
    return recommend_movies
st.markdown("<h1>MOVIE RECOMMENDER SYSTEM</h1>",unsafe_allow_html=True)
select_movie = st.selectbox('Choose the movie to get similar recommendations:',movies['title'].values)
if st.button('Recommend'):
    with st.spinner('Fetching Recommendations....'):
        time.sleep(1.5)
        recommendations = recommend(select_movie)
        st.success('Here are some similar movies:')
        for movie in recommendations:
            st.markdown(
                f"""
                <div style="
                    background-color: #222;
                    padding: 10px;
                    margin: 5px 0;
                    border-radius: 8px;
                    font-size: 18px;
                    font-weight: bold;
                    color: #FFD700;
                ">
                    🎬 {movie}
                </div>
                """,
                unsafe_allow_html=True
            )
with st.expander("About this app:"):
    st.write(" This is a simple movie recommender system built using NLP and cosine similarity.Just select a movie you like, and it will suggest 5 similar ones based on keywords, genres, and cast!")
    
