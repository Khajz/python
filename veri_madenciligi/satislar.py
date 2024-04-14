#Linear regrasyon yes mama

import matplotlib.pyplot as plt
import pandas as pd

veriler = pd.read_csv(r'veri_madenciligi\satislar.csv') #CSV okundu
aylar=veriler[['Aylar']] #Aylar değişkenine CSV'deki Aylar sütunu atandı
satislar=veriler[['Satislar']] #Satışlar değişkenine CSV'deki Satislar sütunu atandı

from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(aylar,satislar,test_size=0.33,random_state=0) #Aylar ve Satıslar bilgilerini yapay zeka ile eğitip yeni bilgileri x_train ve y_train değişkenlerine atadık

print(x_train)
print(x_test)

from sklearn.linear_model import LinearRegression

#Lineer Regrasyon
lr = LinearRegression()
lr.fit(x_train,y_train)
print(lr.predict(x_test))
