import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def get_cos_sim(breeds,user):
    cos_sim=cosine_similarity(user,breeds)
    print(cos_sim)
    return cos_sim.argsort()[:, ::-1]

def find_sim_breeds(clients, breeds, sim_df, userId, top_n=10):
    clients.reset_index(inplace=True)
    print(clients)
    print(clients.columns)
    user_id = clients[clients['userId'] == userId]
    print(sim_df)
    print(user_id)

    user_index = user_id.index.values
    print("user_index=", user_index)
    similar_indexes = sim_df[user_index, :(top_n)]

    # 추출된 top_n index들 출력. top_n index는 2차원 데이터 임.
    #dataframe에서 index로 사용하기 위해서 1차원 array로 변경
    print(similar_indexes)
    similar_indexes = similar_indexes.reshape(-1)

    return breeds.iloc[similar_indexes]
