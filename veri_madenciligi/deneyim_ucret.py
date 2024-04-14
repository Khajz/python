import pandas as pd
import matplotlib.pyplot as plt
import numpy
from sklearn.metrics import r2_score

du = pd.read_csv(r'C:\Kodlarz\PythonCV\veri_madenciligi\deneyim_ucret.csv', header=0, sep=";") #CSV'nin okunması

x = du['Deneyim'] #Deneyim yılları x değişkenine atandı
y = du['Ucret'] #Ücret y değişkenine atandı

modelim = numpy.poly1d(numpy.polyfit(x,y,1)) #Grafik eğrisi 
cizgim = numpy.linspace(1,11,100) #Grafik çizgisi

print(r2_score(y,modelim(x))) #Üretilen grafiğin modele orantılı doğruluğu

#Oluşturulan modele göre tahmini maaşları
print(f"4 Yıl deneyimi olan birisinin alacağı tahmini maaş: {modelim(4)}")
print(f"8 Yıl deneyimi olan birisinin alacağı tahmini maaş : {modelim(8)}")
print(f"2o Yıl deneyimi olan birisinin alacağ tahmini maaş : {modelim(20)}")

#Grafik Yazdırma
plt.scatter(x, y)
plt.plot(cizgim, modelim(cizgim),color="purple",linewidth = "2.5")
plt.show()