# -*- coding: utf-8 -*-
"""
Created on Tue May 12 22:18:13 2020

@author: MEET
"""

import pickle as pkl
import tempfile
from pathlib import Path

# Opening the pickled models which were trained using apriori algo
action = pkl.load( open( "model/action.p", "rb" ) )
romance = pkl.load( open( "model/romance.p", "rb" ) )
magic = pkl.load( open( "model/magic.p", "rb" ) )
thrill = pkl.load( open( "model/thrill.p", "rb" ) )
horror = pkl.load( open( "model/horror.p", "rb" ) )
comedy =pkl.load( open( "model/comedy.p", "rb" ) )

# list of movies
action_list = pkl.load( open ("model/action_list.p","rb"))
romance_list = pkl.load( open ("model/romance_list.p","rb"))
horror_list = pkl.load( open ("model/horror_list.p","rb"))
thrill_list = pkl.load( open ("model/thrill_list.p","rb"))
magic_list = pkl.load( open ("model/magic_list.p","rb"))
comedy_list = pkl.load( open ("model/comedy_list.p","rb"))
list_of_movies=pkl.load(open('model/list_of movies.p','rb'))

# removing duplicates in list
def remove_duplicates(l:list):
    return list(dict.fromkeys(l).keys())

# main recommend Fucntions
def recommend(movie_name:str):
    movie_name=[movie_name]
    if movie_name in action_list:
        model=action
    elif movie_name in romance_list:
        model=romance
    elif movie_name in horror_list:
        model=horror
    elif movie_name in thrill_list:
        model=thrill
    elif movie_name in magic:
        model =magic
    else:
        model=comedy
    i=0
    j=0
    recommend=[]
    movie_name=movie_name.pop()
    for j in model:
        if movie_name in j:
            recommend.extend(j)
            recommend=remove_duplicates(recommend)
    if movie_name in recommend:
        recommend.remove(movie_name)
    if 'nan' in recommend:
        recommend.remove('nan')
    return recommend

#############Using Recommender function#############
# print(recommend('Aladdin(2019)'))

'''
for m in ['action','romance','horror','magic','thrill','comedy']:
    model=pd.read_csv(m+'.csv',header=None)
    transactions = []
    for i in range(0, model.shape[0]):
        transactions.append([str(model.values[i,j]) for j in range(0, model.shape[1])])

    pkl.dump(transactions,open(m+'_list.p','wb'))
'''
