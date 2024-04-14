import pandas as pd
import matplotlib.pyplot as plt
import numpy
from sklearn.metrics import r2_score

ps = pd.read_csv(r'C:\Kodlarz\PythonCV\veri_madenciligi\position_salaries.csv', header=0, sep=",") #CSV'nin okunması

x=ps['Level'] #Pozisyon-Level ilişkisi x değişkenine atandı
y=ps['Salary'] #Maaş y değişkenine atandı

modelim = numpy.poly1d(numpy.polyfit(x,y,3)) #Grafik Eğrisi
cizgim = numpy.linspace(1,22,100) #Grafik çizgisi

print(r2_score(y,modelim(x))) # Grafiğin doğruluk skoru

print(modelim(4)) #Müdür rolünün tahmini ücreti

#Grafiğin yazılması
plt.scatter(x, y)
plt.plot(cizgim, modelim(cizgim),color="purple",linewidth = "2.5")
plt.show()