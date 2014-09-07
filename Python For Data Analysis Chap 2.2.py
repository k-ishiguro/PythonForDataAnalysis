# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

# <codecell>

# tags for attributes
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('pydata-book/ch02/movielens/users.dat', sep='::', header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('pydata-book/ch02/movielens/ratings.dat', sep='::', header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('pydata-book/ch02/movielens/movies.dat', sep='::', header=None, names=mnames)

# <codecell>

users[:5]

# <codecell>

ratings[:5]

# <codecell>

movies[:5]

# <codecell>

# given the attribute (column) names, pandas automatically joins tables
data = pd.merge(pd.merge(ratings, users), movies)
print type(data)
print data.shape

# <codecell>

data[:5][:]

# <codecell>

mean_rating = data.pivot_table('rating', rows='title', cols="gender", aggfunc='mean') # for each title and each gender, compute the average of ratings

# <codecell>

mean_rating[:5]

# <codecell>

temp = data.groupby('title') # aggregate by "title" keys??
ratings_by_title = temp.size() # and its sizes
ratings_by_title[:10]

# <codecell>

active_titles = ratings_by_title.index[ratings_by_title >= 250] # key is title. thus index is title
active_titles

# <codecell>

active_mean_rating = mean_rating[active_titles] # this is invalid

# <codecell>

mean_ratings = mean_rating.ix[active_titles]

# <codecell>

mean_ratings

# <codecell>

top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)

# <codecell>

top_female_ratings[:10]

# <codecell>

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_index(by='diff')
sorted_by_diff[:10]

# <codecell>

rating_std_by_title = data.groupby('title')['rating'].std() # aggregate all by key='title', looking at the aggregated 'rating' cell, then compute its s.t.d.
rating_std_by_title = rating_std_by_title.ix[active_titles]
rating_std_by_title.order(ascending=False)[:10]

# <codecell>


