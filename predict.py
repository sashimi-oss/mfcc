import os
import numpy as np
import pandas as pd
import librosa
from pycaret.classification import *
import my_pycar



y, sr = librosa.load('./audio/voice1/line1.wav')
mfcc = librosa.feature.mfcc(y=y, sr=sr)

mfcc = np.average(mfcc, axis=1)
mfcc = mfcc.flatten()
mfcc = mfcc.tolist()
mfcc = mfcc[1:13]
X_data = []
X_data.append(mfcc)
y_data = []
y_data.append('line1')#speakernum

X = pd.DataFrame(X_data, columns=[f'mfcc_{n}' for n in range(1, 13)])
y = pd.DataFrame({'target': y_data})
df = pd.concat([X, y], axis=1)
df.to_csv('predict.csv', index=False)  # csvで保存
df.head()

#dfって打ったら結果出るのかな？


#必要ならmy_pycar.pyの処理をコピペする
#多分my_pycar.final_modelで行ける気がする
predict = pd.read_csv('predict.csv')

pred = predict_model(my_pycar.final_model, data = predict)
print(pred)