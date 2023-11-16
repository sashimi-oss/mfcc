import numpy as np
import pandas as pd
from pycaret.classification import *

data = pd.read_csv('./rec-ojii-mfcc.csv')
data['target'] = data['target'] - 1
data.head()

reg = setup(data=data,
           target='target',
           data_split_shuffle=True,
           use_gpu=True,
           fold=5,
           n_jobs=-1)

compare_models(exclude=['catboost', 'xgboost', 'gbc', 'rf'])