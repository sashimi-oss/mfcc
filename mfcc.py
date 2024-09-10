import os
import numpy as np
import pandas as pd
import librosa

X_data = []  # 特徴行列
y_data = []  # クラスラベルデータ

men = [1,3,4,8,9]
women = [2,5,6,7,10]
spkCnt = 0
# list(map(lambda x : x-1, women)) # 無名関数の書き方

# for speaker_num in range(1, 11):  #voice1~10 
# for speaker_num in men:  #1,3,4,8,9 
for speaker_num in women:  #2,5,6,7,10
    spkCnt += 1
    # parallel100の音声データが入っているディレクトリ名
    # dir_name = f'./jvs_ver1/jvs{str(speaker_num).zfill(3)}/parallel100/wav24kHz16bit'
    # if speaker_num in men:
    #     continue
    dir_name = f'./audio/voice{speaker_num}'
    for file_name in os.listdir(dir_name):
        file_path = os.path.join(dir_name, file_name)  # 音声ファイルへのパス
        y, sr = librosa.load(file_path)  # 音声ファイルを読み込む
        mfcc = librosa.feature.mfcc(y=y, sr=sr)  # MFCC
        mfcc = np.average(mfcc, axis=1)  # 時間平均を取る
        mfcc = mfcc.flatten()
        mfcc = mfcc.tolist()
        mfcc = mfcc[1:13]  # 低次の係数を取り出す（12次まで取り出すことが多い）
        X_data.append(mfcc)
        y_data.append(spkCnt)


X = pd.DataFrame(X_data, columns=[f'mfcc_{n}' for n in range(1, 13)])
y = pd.DataFrame({'target': y_data})

df = pd.concat([X, y], axis=1)
df.to_csv('mfcc.csv', index=False)  # csvで保存
df.head()