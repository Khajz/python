def aritort(sayilar):
    ort=(sum(sayilar))/len(sayilar)
    print(f"Girilen sayıların aritmetik ortalaması: {ort}")
def geoort(sayilar):
    carpim=1
    for sayi in sayilar:
        carpim=carpim*sayi
    ort=((carpim)**(1/len(sayilar)))
    print(f"Girilen sayıların geometrik ortalaması: {round(ort,1)}")
def harort(sayilar):
    toplam=0
    for sayi in sayilar:
        toplam+=1/sayi
    ort=len(sayilar)/toplam
    print(f"Girilen sayıların harmonik ortalaması: {round(ort,1)}")

sayilar=[]
x=int(input("Kaç tane sayı girmek istersiniz?: "))

for i in range(x):
    sira=i+1
    a=int(input(f"{sira}. Sayıyı giriniz!: "))
    sayilar.append(a)
aritort(sayilar)
geoort(sayilar)
harort(sayilar)