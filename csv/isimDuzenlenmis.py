import csv

with open('csv\\isim.csv','r',newline='') as file:
    fileEncoding="UTF-8-BOM"
    okuma=csv.reader(file)
    satirlar=list(okuma)
    print(satirlar)
    
    for satir in satirlar:
        birlesmis=[str(satir[0])+str(satir[2])+str(satir[4])]
        satir[0]=birlesmis
        del satir[2]
        del satir[3]
    with open('csv\\isim_duzenlenmis.csv','w',newline='') as file1:
        yazici=csv.writer(file1)
        yazici.writerows(satirlar)
        
