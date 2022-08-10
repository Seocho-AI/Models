import pandas as pd
import numpy as np
import client
import similarity_func
import validation

breeds=pd.read_csv('breeds.csv',index_col=0)
print(breeds.head())
