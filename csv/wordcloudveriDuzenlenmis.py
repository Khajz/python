import csv

with open('csv\\wordcloudveri.csv','r',newline='') as dosya:
    csvokuyucu=csv.reader(dosya)
    for row in csvokuyucu:
        if 'CNSV' in row:
            with open('csv\\wordcloudveri_duzenlenmis.csv','a',newline='') as dosya1:
                writer=csv.writer(dosya1)
                writer.writerow(row)
