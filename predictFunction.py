import os
import numpy as np
import pandas as pd
import librosa
from pycaret.classification import *
import pickle


def predictPostAudio(whichModel):

    with open(whichModel, mode='rb') as f:
        final_model = pickle.load(f)

    y, sr = librosa.load('./audio/uploaded.wav')
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

    numbers = pred.prediction_label[0]

    print(pred)
    print(numbers)

    vcAct = {0:"男の子", 1:"少年", 2:"青年男",
            3:"おじさん", 4:"おじいさん", 5:"女の子",
            6:"少女", 7:"青年女", 8:"おばさん", 9:"おばあさん"}
    # vcAct = ['男の子', '少年', '青年男', 'おじさん', 'おじいさん', '女の子', '少女', '青年女', 'おばさん', 'おばあさん']

    if numbers in vcAct:
        preVC = vcAct[numbers]
    else:
        print("エラー")

    return preVC