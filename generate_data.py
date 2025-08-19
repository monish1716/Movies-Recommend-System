import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from ast import literal_eval

# Helper functions
def convert(obj):
    L = []
    for i in literal_eval(obj):
        L.append(i['name'])
    return L

def convert3(obj):
    L = []
    counter = 0
    for i in literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter += 1
        else:
            break
    return L

def fetch_director(obj):
    L = []
    for i in literal_eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L

def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ""

# Load and merge data
movies_df = pd.read_csv("tmdb_5000_movies.csv")
credits_df = pd.read_csv("tmdb_5000_credits.csv")
movies_df = movies_df.merge(credits_df, on='title')

# Select relevant features
features = ['genres', 'keywords', 'cast', 'crew']
for feature in features:
    movies_df[feature] = movies_df[feature].apply(literal_eval)

# Apply helper functions
movies_df['cast'] = movies_df['cast'].apply(convert3)
movies_df['crew'] = movies_df['crew'].apply(fetch_director)
movies_df['genres'] = movies_df['genres'].apply(convert)
movies_df['keywords'] = movies_df['keywords'].apply(convert)

# Create a new column with all combined features
movies_df['features'] = movies_df['genres'].apply(clean_data) + \
                      movies_df['keywords'].apply(clean_data) + \
                      movies_df['cast'].apply(clean_data) + \
                      movies_df['crew'].apply(clean_data)
movies_df['features'] = movies_df['features'].apply(lambda x: " ".join(x))

# Create a TfidfVectorizer and compute the cosine similarity matrix
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies_df['features'])
similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Prepare data for the app
movies_df = movies_df[['movie_id', 'title']]

# Save the processed data
with open('movie_dict.pkl', 'wb') as f:
    pickle.dump(movies_df.to_dict(), f)

with open('similarity.pkl', 'wb') as f:
    pickle.dump(similarity, f)

print("Data generation complete. The files movie_dict.pkl and similarity.pkl have been created.")