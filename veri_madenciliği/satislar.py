#Linear regrasyon yes mama

import matplotlib.pyplot as plt
import pandas as pd

veriler = pd.read_csv(r'C:\Kodlarz\Python\VeriMadencilik\satislar.csv')
aylar=veriler[['Aylar']]
satislar=veriler[['Satislar']]

from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(aylar,satislar,test_size=0.33,random_state=0)

print(x_train)
print(x_test)