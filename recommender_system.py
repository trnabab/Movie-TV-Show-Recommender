import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests

# Load the cleaned dataset
file_path = 'cleaned_netflix_titles.csv'
netflix_df = pd.read_csv(file_path)

# Combine relevant metadata into a single string
netflix_df['metadata'] = netflix_df[['title', 'director', 'cast', 'country', 'listed_in']].fillna('').agg(' '.join, axis=1)

# Compute the TF-IDF matrix
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(netflix_df['metadata'])

# Compute the cosine similarity matrix for content-based filtering
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get content-based recommendations
def get_recommendations(title, cosine_sim=cosine_sim):
    try:
        idx = netflix_df[netflix_df['title'].str.contains(title, case=False, na=False)].index[0]
    except IndexError:
        return ["Title not found"], [], []

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    titles = netflix_df['title'].iloc[movie_indices].tolist()
    posters = [get_poster(title) for title in titles]
    links = [f'https://www.netflix.com/search?q={title.replace(" ", "%20")}' for title in titles]
    return titles, posters, links

# Function to fetch poster URLs from OMDb API
def get_poster(title):
    api_key = '73ef2faf'  # Replace with your OMDb API key
    url = f'http://www.omdbapi.com/?t={title}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data['Poster'] if 'Poster' in data else None
