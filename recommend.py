# -*- coding: utf-8 -*-
"""
Created on Tue May 12 22:18:13 2020

@author: MEET
"""

import pickle as pkl
import tempfile
from pathlib import Path

# Opening the pickled models which were trained using apriori algo
action = pkl.load( open( "dataset/action.p", "rb" ) )
romance = pkl.load( open( "dataset/romance.p", "rb" ) )
magic = pkl.load( open( "dataset/magic.p", "rb" ) )
thrill = pkl.load( open( "dataset/thrill.p", "rb" ) )
horror = pkl.load( open( "dataset/horror.p", "rb" ) )
comedy =pkl.load( open( "dataset/comedy.p", "rb" ) )

# list of movies
action_list = pkl.load( open ("dataset/action_list.p","rb"))
romance_list = pkl.load( open ("dataset/romance_list.p","rb"))
horror_list = pkl.load( open ("dataset/horror_list.p","rb"))
thrill_list = pkl.load( open ("dataset/thrill_list.p","rb"))
magic_list = pkl.load( open ("dataset/magic_list.p","rb"))
comedy_list = pkl.load( open ("dataset/comedy_list.p","rb"))
list_of_movies=pkl.load(open('dataset/list_of movies.p','rb'))

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
    dataset=pd.read_csv(m+'.csv',header=None)
    transactions = []
    for i in range(0, dataset.shape[0]):
        transactions.append([str(dataset.values[i,j]) for j in range(0, dataset.shape[1])])
    
    pkl.dump(transactions,open(m+'_list.p','wb'))        
'''      
        
        
        
        

        
        
        