import pandas as pd
import numpy as np

def client_survey(client_df, user):
    global client
    for column in user.keys():
        if column!='userId':
            user[column]=np.random.randint(0,6)

    updated_clients=pd.concat([client_df ,user])
    return updated_clients
