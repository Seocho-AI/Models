import pandas as pd
import numpy as np
import client as cl
import similarity_func
import validation
from pathlib import Path


if __name__== "__main__":
    breeds=pd.read_csv('dogbreeds-master/breeds.csv', index_col=0)
    if Path('dogbreeds-master/breeds.csv')==False:
    clients=pd.read_csv('clients.csv', index_col=0)
    clients=clients.T
    clients.to_csv('clients.csv')
    userId=input("userID: ")

    client={}
    client['userId']=userId

    for column in breeds.columns:
        client[column]=0
    print(client)
    client=pd.Series(client)

    clients=cl.client_survey(client, client)
    client.set_index('userId')
    print(client)
    client.to_csv('clients.csv')

