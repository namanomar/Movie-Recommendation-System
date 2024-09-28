# 🎬 Movie Recommendation System

Welcome to the **Movie Recommendation System**! This app helps users find movies they'll love based on cosine similarity between movie features. With a user-friendly interface built using Streamlit and powerful machine learning techniques using PyTorch, we provide personalized movie suggestions.

## 🚀 Features
- **Movie Recommendations**: Get personalized movie suggestions based on cosine similarity.
- **Poster Fetching**: Movie posters are fetched using movie IDs.
- **Interactive UI**: Streamlit interface that allows users to easily explore recommendations.
- **PyTorch Integration**: Utilizes PyTorch for model building and computation.

## ⚙️ How It Works
1. **Data Preprocessing**: We use movie metadata (e.g., genre, actors, directors) and extract relevant features.
2. **Cosine Similarity**: Movie features are compared using cosine similarity to recommend movies similar to the one chosen by the user.
3. **Streamlit App**: The UI allows users to select a movie, view recommendations, and fetch movie posters dynamically.

## 🛠️ Tech Stack

| Technology | Description |
|------------|-------------|
| ![Streamlit](https://img.shields.io/badge/Streamlit-black?style=for-the-badge&logo=streamlit) | Frontend interface for the recommendation system. |
| ![PyTorch](https://img.shields.io/badge/PyTorch-red?style=for-the-badge&logo=pytorch) | Backend for model computation and deep learning. |
| ![Pandas](https://img.shields.io/badge/Pandas-blue?style=for-the-badge&logo=pandas) | Data manipulation and preprocessing. |
| ![Pickle](https://img.shields.io/badge/Pickle-lightgreen?style=for-the-badge&logo=python) | Serializing and loading the trained recommendation model. |

## 📦 Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/movie-recommendation-system.git
    cd movie-recommendation-system
    ```

2. **Install Dependencies**:
    You can install all the required libraries via `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit App**:
    Once the dependencies are installed, you can run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## 🎯 Key Components

### 1. Cosine Similarity
We use cosine similarity to compute the similarity between movie vectors. Movies with a higher cosine similarity score are recommended.

### 2. PyTorch Model
While the recommendation system is based on cosine similarity, we utilize PyTorch to handle matrix operations and ensure efficient computations.

### 3. Movie Poster Fetching
We use the movie ID to dynamically fetch and display movie posters to enhance the user experience.

## 🖥️ Usage

1. Run the app using Streamlit.
2. Select a movie from the dropdown or search for a movie title.
3. View the list of similar movies and their posters.

## 📊 Example Output

```python
# Example of using cosine similarity for recommendation:
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Assuming 'movies_df' contains the movie feature vectors
cosine_sim = cosine_similarity(movies_df)
