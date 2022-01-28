#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Build a movie recomendation engine using python


# In[1]:


#import the libraries 
import re
import pandas as pd 
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split


# In[2]:


# Load the data into movies_df
movies_df = pd.read_csv("title.basics.tsv", sep='\t')
print(f'Exploring data of {movies_df.shape[0]} Rows and {movies_df.shape[1]}')
# movies_df.head(n=3)


# In[3]:


# Split the data into train and test 
train, test = train_test_split(movies_df, test_size=0.1,shuffle=False)
# create a Id column dynamically
test['Movie_id'] = range(0,test.shape[0])
# Now the added column will be our new index for test
test=test.set_index('Movie_id')
# test.shape


# In[4]:


#Select the most important colums in your Data
columns = ['genres','originalTitle','isAdult','primaryTitle']


# In[5]:


test[columns].tail(10)


# In[6]:


#Check for any missing values in the important columns
if test[columns].isnull().values.any():
    test=test.dropna()
test[columns].isnull().values.any()


# In[7]:


#Combine the important colums into a single string
def get_important_features(data):
    important_features = []
    for index,row in data.iterrows():
        new_column = re.sub('[^A-Za-z0-9]+', ' ',row['genres']) + ' ' + re.sub('[^A-Za-z0-9]+', ' ',row['originalTitle']) 
        + ' ' +re.sub('[^A-Za-z0-9]+', ' ',row['primaryTitle'])        +' '+str(row['isAdult'])
        important_features.append(new_column.lower())
    return important_features


# In[8]:


#Create a column to hold the combined strings
test["important_features"] = get_important_features(test)

#show the resulted data
test.head(30)


# In[9]:


#Convert the text to a matrix of token counts 
cm = CountVectorizer().fit_transform(test['important_features'])


# In[10]:


#Get the cosine similraity matrix from the count matrix
cs = cosine_similarity(cm)
print(cs)


# In[11]:


#Get the shape of the cosine similar
cs.shape


# In[12]:


#Get the title of the movie to compare with
test_title ="Art of Falling in Love"

#Find the movie id 
movie_id = test[test.originalTitle==test_title].index.values[0]
print(movie_id)


# In[13]:


#Create a list of enumeration of the movies similarity scores [(movie_id, similarity_score)]
scores = list(enumerate(cs[movie_id]))
print(scores)


# In[14]:


#Sort the list
sorted_scores = sorted(scores, key = lambda x:x[1], reverse= True)
sorted_scores = sorted_scores[1:]
print(sorted_scores)


# In[18]:


#Create a loop to print the top 10 similar movies 
j=0
print('Top ten recomendations to movie (', test_title,') are:\n')
for item in sorted_scores:
    movie_title = test[test.index ==item[0]]['originalTitle'].values[0]
    print(j,movie_title)
    j=j+1
    if j>10:
        break
    


# In[55]:


def sort_scores(movie_id):
    scores = list(enumerate(cs[movie_id]))
    #Sort the list
    sorted_scores = sorted(scores, key = lambda x:x[1], reverse= True)
    return sorted_scores[1:]

def print_top_ten(sorted_scores, movie_title):
    #Create a loop to print the top 10 similar movies 
    j=0
    print('Top ten recomendations to movie (', movie_title,') are:\n')
    for item in sorted_scores:
        movie_title = test[test.index ==item[0]]['originalTitle'].values[0]
        print(j,movie_title)
        j=j+1
        if j>10:
            break
    
def see_top_ten_movies_for(some_movie):
    print('----------------------------------')
    print('Looking for the movie: '+ some_movie)
    movie_id = None
    try:
    #Find the movie id 
        movie_id = test[test.originalTitle==some_movie].index.values[0]
    except:
        print('Movie not Found')
    if movie_id is not None:
        print('Found it!')
        scores = sort_scores(movie_id)
        print_top_ten(scores, some_movie)
    print('----------------------------------')
        


# In[59]:


see_top_ten_movies_for('Star Wars')


# In[60]:


see_top_ten_movies_for('Alien Galaxy')


# In[61]:


see_top_ten_movies_for('Fast Cars')


# In[11]:


import csv
with open('title.basics.tsv', 'r') as inp, open('title.basics_result.tsv', 'w') as out:
    writer = csv.writer(out,delimiter="\t")
    firstline=True
    for row in csv.reader(inp,delimiter="\t"):
        if firstline:    #skip first line
            firstline = False
            writer.writerow(row)
            continue
        else:
            if "Episode" not in row[2] and 'Movie' in row[1]:
                writer.writerow(row)


# In[ ]:





# In[ ]:





# In[53]:


test[test['primaryTitle'].str.contains('Alien')].head(40)


# In[ ]:




