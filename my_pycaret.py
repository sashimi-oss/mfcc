import numpy as np
import pandas as pd
from pycaret.classification import *
import pickle

data = pd.read_csv('./mfcc.csv')
data['target'] = data['target'] - 1
data.head()

reg = setup(data=data,
           target='target',
        #    preprocess=False,
           data_split_shuffle=True,
           use_gpu=True,
           fold=10,
           n_jobs=-1,
           )

#compare_models(exclude=['catboost', 'xgboost', 'gbc', 'rf'])
compare_models()

# model = create_model('qda')
model = create_model('lda')
# model = create_model('nb')
# model = create_model('et')
tuned_model = tune_model(model, optimize = 'AUC')
# tuned_model = tune_model(model, optimize = 'F1')
evaluate_model(tuned_model)
final_model = finalize_model(tuned_model)

predict_model(final_model)

#学習モデルの保存　↓書き出すモデルの名前
with open('shuurokuSssLdaMen.pickle', mode='wb') as f:
    pickle.dump(final_model,f,protocol=-1)