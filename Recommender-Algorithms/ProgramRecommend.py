"""
Test Recommender Engine
"""

import pandas as pd
import graphlab

u_cols = ['user_d', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('u.user', sep='|', names=u_cols, encoding='latin-1')

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('u.data', sep='\t', names=r_cols, encoding='latin-1')

i_cols = ['movie id', 'movie title', 'release date', 'video release date',
        'IMDb URL', 'unknown', 'Action', 'Adventure',
        'Animation', 'Children\'s','Comedy', 'Crime', 'Documentary',
        'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery',
        'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items = pd.read_csv('u.item', sep = '|', names=i_cols,
        encoding='latin-1')

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings_base = pd.read_csv('ua.base', sep='\t', names=r_cols, encoding='latin-1')
ratings_test = pd.read_csv('ua.test', sep='\t', names=r_cols, encoding='latin-1')

train_data = graphlab.SFrame(ratings_base)
test_data = graphlab.SFrame(ratings_test)

popularity_model = graphlab.popularity_recommender.create(train_data, user_id='user_id', item_id='movie_id', target='rating')

popularity_recommendation = popularity_model.recommend(users=range(1,6), k=5)
popularity_recommendation.print_rows(num_rows=25)

ratings_base.groupby(by='movie_id')['rating']
