import pandas as pd
import matplotlib.pyplot as plt
health_data = pd.read_csv(r'C:\Kodlarz\PythonCV\veri_madenciligi\health_data.csv', header=0, sep=";") #CSV okunması

health_data.dropna(axis=0,inplace=True) #Boş değerler silindi

print(health_data.to_string()) #Datanın terminalden okunması için stringe çevrildi

health_data["Average_Pulse"]=health_data['Average_Pulse'].astype(float) #Obje tipleri floata çevrildi
health_data["Max_Pulse"] =health_data["Max_Pulse"].astype(float)#Obje tipleri floata çevrildi

#Grafik Çizdirme
health_data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='line')
plt.show()
