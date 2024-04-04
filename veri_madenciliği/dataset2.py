import pandas as pd

df = pd.read_csv(r'C:\Kodlarz\Python\VeriMadencilik\dataset2.csv')

calort = df["Calories"].mean() #Kalorilerin ortalamasını alıp bunu bir değişkene atadık
df['Calories'].fillna(calort,inplace=True) #Kalorideki boş olan değerlere diğerlerinin ortalamasını yazdık

df.loc[22,'Date'] = '2020-12-22' #Eksik tarihi kendimiz doğru pozisyona, doğru tarih olacak şekilde ekledik
df['Date'] = pd.to_datetime(df['Date'],format='mixed') #Tarihteki yanlış formatları düzeltti

durort= df['Duration'].mean() #Sürelerin ortalamsını aldık
for x in df.index:
    if df.loc[x,'Duration']>60 or df.loc[x,'Duration']<15: #Absürt zamanları kontrol et
        df.loc[x,'Duration']=durort #Absürt zamanları ortalama zamanlar ile değiştir

df.drop_duplicates(inplace=True) #Tekrar eden verileri siler
        

print(df.to_string())#Dataframe'i yazdırdı