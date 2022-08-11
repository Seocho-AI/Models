import pandas as pd
import numpy as np
import clientData as cl
import similarity_func
import validation
from pathlib import Path

def preprocessing():
    #clients=clients.dropna()
    #clients.set_index('userId',inplace=True)
    global breeds, clients
    breeds=pd.read_csv('dogbreeds-master/breeds.csv').set_index('breed')
    clients=pd.read_csv('clients.csv', index_col=0).set_index('userId')
    # del clients['url']
    # del clients['breed_group']
    # del clients['height']
    # del clients['weight']
    # del clients['life_span']
    #print(clients)
    userId=int(input("userID: "))

    client={}
    client['userId']=userId

    # for column in breeds.columns:
    #     client[column]=0
    #print(client)
    #print(clients)
    # client=pd.Series(client)
    clients.reset_index(inplace=True)
    clients=cl.client_survey(clients, client)

    #print(clients)
    clients.set_index('userId')
    clients.to_csv('clients.csv')

if __name__== "__main__":
    breeds=pd.read_csv('dogbreeds-master/breeds.csv').set_index('breed')
    clients=pd.read_csv('clients.csv', index_col=0).set_index('userId')

    breeds=breeds.loc[:,"a_adaptability" : "e4_potential_for_playfulness"]
    clients=clients[clients.index.notnull()]
    # print(breeds.shape, clients.shape)
    #
    # print(breeds.columns)
    # print(clients.columns)
    # print(clients)
    # print(breeds.head())
    # print(clients.index)
    clients.index=clients.index.astype(dtype='int64', copy=True)
    # print()
    # print(clients.index)
    #print(clients[clients.loc[,]])
    #clients=clients.sort_index()


    # using cosine similarity
    sim_df=similarity_func.get_cos_sim(breeds, clients)
    #print(sim_df)
    userId=9
    recBreeds=similarity_func.find_sim_breeds(clients=clients, breeds=breeds, sim_df=sim_df, userId=userId, top_n=10)
    print(recBreeds)
    print(clients[clients['userId']==userId])
    user=clients.loc[clients['userId']==userId].set_index('userId')
    print(user)
    print("user's rating mean: \n",user.mean(axis=1))
    print()
    validation.RMSE(user=user, recBreeds=recBreeds)
    print()
    validation.NDCG(user=user, recBreeds=recBreeds)
