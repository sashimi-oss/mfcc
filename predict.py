import os
import numpy as np
import pandas as pd
import librosa
from pycaret.classification import *
import pickle

with open('all.pickle', mode='rb') as f:
    final_model = pickle.load(f)


y, sr = librosa.load('./audio/uploaded.wav')#変更せな
mfcc = librosa.feature.mfcc(y=y, sr=sr)

mfcc = np.average(mfcc, axis=1)
mfcc = mfcc.flatten()
mfcc = mfcc.tolist()
mfcc = mfcc[1:13]
X_data = []
X_data.append(mfcc)
y_data = []
y_data.append('speaker')#speakernum

X = pd.DataFrame(X_data, columns=[f'mfcc_{n}' for n in range(1, 13)])
y = pd.DataFrame({'target': y_data})
df = pd.concat([X, y], axis=1)
df.to_csv('predict.csv', index=False)  # csvで保存
df.head()

predict = pd.read_csv('predict.csv')

pred = predict_model(final_model, data = predict)
print(pred)
