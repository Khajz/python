import csv
with open('csv\\adresler.csv','r',newline='') as file:
    okuma=csv.reader(file)
    satirlar=list(okuma)
    
    for satir in satirlar:
        birlesmis=satir[4] + '-' + satir[5]
        satir[4]=birlesmis
        del satir[5]
    
    with open('csv\\adresler_duzenlenmis.csv','a',newline='') as file1:
        yazici=csv.writer(file1)
        yazici.writerow(['İsim','Soyisim','Adres','İl','İlçe-PK'])
        yazici.writerows(satirlar)
