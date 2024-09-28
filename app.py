import zipfile
import pandas as pd
import streamlit as st
import pickle
import requests
from PIL import Image
from io import BytesIO
import os
from dotenv import load_dotenv
load_dotenv()
MY_ENV_VAR = os.getenv('apikey')
def unzip_file_if_not_exists(zip_file_path, extract_to_dir):
    # Check if the directory already exists
    if not os.path.exists(extract_to_dir):
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to_dir)
    else:
        print(f"Directory '{extract_to_dir}' already exists. No extraction needed.")

zip_file_path = 'similarity.zip'  
extract_to_dir = 'similarity_files'  

unzip_file_if_not_exists(zip_file_path, extract_to_dir)

def fetch_poster(movie_id):
    response = requests.get('https://www.omdbapi.com/?t={}&apikey={}'.format(movie_id,MY_ENV_VAR))
    data = response.json()
    
    # Check if the Poster field exists
    if 'Poster' in data and data['Poster'] != "N/A":
        poster_url = data["Poster"]
        img_response = requests.get(poster_url)
        img = Image.open(BytesIO(img_response.content))
        return img  # Return the image object to display
    
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    fetch_poster(movie_index)
    recommended_movies = []
    recommended_movies_posters = []
    for x in movies_list:
        movie_id = movies.iloc[x[0]].movie_id
        recommended_movies.append(movies.iloc[x[0]].title)
        
        # Fetch poster and handle cases where no poster is found
        poster = fetch_poster(movie_id)
        if poster:
            recommended_movies_posters.append(poster)
        else:
            recommended_movies_posters.append("empty.png")
        
        
    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('./similarity_files/similarity.pkl', 'rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
