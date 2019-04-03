#Primaditaningtyas W
#primaditaningtyas.w@gmail.com
#Ref dan data :https://towardsdatascience.com/solving-a-simple-classification-problem-with-python-fruits-lovers-edition-d20ab6b071d2
# Package yg dibutuhkan

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib
import sys

option = sys.argv[1]
parameter = sys.argv[2]



if option == 'train':
    buah = pd.read_csv(parameter, sep='\t')
    elemen = ['mass','width','height','color_score']
    X = buah[elemen]
    y = buah['fruit_label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    X_test.to_csv('X_test.txt', index=None)

    X_train = X_train.astype('float64')
    X_test = X_test.astype('float64')
    scaler = MinMaxScaler()
    X_train_scl = scaler.fit_transform(X_train)
    X_test_scl = scaler.transform(X_test)

    knn = KNeighborsClassifier()
    knn.fit(X_train_scl, y_train)
    
    joblib.dump(knn, 'knn_mod.joblib')

    print('Akurasi K-NN classifier pada data training',round(knn.score(X_train_scl, y_train),2))
    print('Akurasi K-NN classifier pada data test',round(knn.score(X_test_scl, y_test),2))
elif option == 'test':

    X_test_load = pd.read_csv(parameter, sep=',')
    X_test_load_float = X_test_load.astype('float64')   
    scaler = MinMaxScaler()
    X_test_load_scl = scaler.fit_transform(X_test_load_float)   
    r,c = X_test_load.shape

    print("Masukkan nilai baris antara ", 1, " sampai ",r )

    data_ke = input('Data ke: ')
    data_ke = int(data_ke)
    c = data_ke-1
    knn_mod = joblib.load('knn_mod.joblib')

    result = knn_mod.predict([X_test_load_scl[c]])
    print(X_test_load.iloc[c])
    print("ID : ", result)
    if result == [1]:
        print('Apel')
    elif result == [2]:
        print('Mandarin')
    elif result == [3]:
        print('Orange')
    else:
        print('Lemon')
else:
    print('Masukkan input setting (tanpa tanda petik) setelah index.py diikuti file yang akan diproses: ')
    print('"train" untuk membuat model')
    print('"test" untuk menguji data test')