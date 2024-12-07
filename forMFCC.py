import os
import numpy as np
import pandas as pd
import librosa
from pycaret.classification import *
import pickle


def forAudioTest(whichModel):

    with open(whichModel, mode='rb') as f:
        final_model = pickle.load(f)
    
    dir_name = f'./audio/audio_test2'
    wavList = os.listdir(dir_name)

    # y, sr = librosa.load('./audio/uploaded.wav')
    # y, sr = librosa.load(f'./audio/audio_mabikiSum/sss/sss{forCnt}.wav')
    # y, sr = librosa.load(f'./audio/audio/voice2/line{forCnt}.wav')
    # dir_name = f'./audio/voice1'
    for wavfile in wavList:
        # y, sr = librosa.load(f'./audio/audio_test2/{wavfile}')
        y, sr = librosa.load(os.path.join(dir_name, wavfile))


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
        # df.head()

        predict = pd.read_csv('predict.csv')
        pred = predict_model(final_model, data = predict)
        numbers = pred.prediction_label[0]
        # print(pred)
        # print(numbers)

        vcAct = {0:"男の子", 1:"少年", 2:"成人男性",
                3:"おじさん", 4:"おじいさん", 5:"女の子",
                6:"少女", 7:"成人女性", 8:"おばさん", 9:"おばあさん"}

        if numbers in vcAct:
            preVC = vcAct[numbers]
            print(preVC, '', wavfile)
            # print(preVC)
        else:
            print("エラー")

    return preVC

def forAudioSss(fromCnt, toCnt, whichModel):

    with open(whichModel, mode='rb') as f:
        final_model = pickle.load(f)
    
    for i in range(fromCnt, toCnt+1):
        y, sr = librosa.load(f'./audio/sss/sss{i}.wav')

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
        # df.head()

        predict = pd.read_csv('predict.csv')
        pred = predict_model(final_model, data = predict)
        numbers = pred.prediction_label[0]
        # print(pred)
        # print(numbers)

        vcAct = {0:"男の子", 1:"少年", 2:"成人男性",
                3:"おじさん", 4:"おじいさん", 5:"女の子",
                6:"少女", 7:"成人女性", 8:"おばさん", 9:"おばあさん"}

        if numbers in vcAct:
            preVC = vcAct[numbers]
            # print(f'sss{i}',preVC)
            print(preVC)
        else:
            print("エラー")
        
    return preVC


whichModel = './pickle/mabikiSumLdaMen.pickle'

# print('------実験1後、さらにぴたごえ素材選定------')
print('-----'+whichModel+'-----')

# forAudioSss(0, 366, whichModel)
forAudioTest(whichModel)
