import numpy as np
from sklearn.metrics import ndcg_score
from sklearn.metrics import mean_squared_error

# Root Mean Square Error
def RMSE(user, recBreeds):
    print("RMSE: ")
    for idx in recBreeds.index:
        print(mean_squared_error(user,recBreeds[recBreeds.index==idx])**0.5)

# Normalized Discount Cumulative Gain
def NDCG(user, recBreeds):
    print("NDCG: ")
    for idx in recBreeds.index:
        print(ndcg_score(user, recBreeds[recBreeds.index==idx]))
