import pandas as pd
import numpy as np

def client_survey(client_df, user):
    print("user keys= ",client_df.keys())

    print(client_df)
    for column in client_df.keys():
        if column!='userId':
            user[column]=np.random.randint(1,6)
    user=pd.Series(user, name='userId')
    print(user)

    #print(client_df)
    return client_df.append(user, ignore_index=True)

