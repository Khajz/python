def hesapla(not1,not2,final):
    ortalama=(int(not1)+int(not2)+int(final))/3
    print(f"Ortalama notunuz : {round(ortalama,2)}")
    if ortalama<60 or int(final)<60:
        print(f"Maalesef {round(ortalama,2)} ile kaldınız ")
    else:
        print(f"Tebrikler! {round(ortalama,2)} ile geçtiniz!")

def sayikontrol(sayi):
    try: int(sayi)
    except: return False
    else: return True

n1=input("1.Notunu gir: ")
while sayikontrol(n1)==False or int(n1)<0 or int(n1)>100:
   n1=input("1.Notunu yanlış girdin tekrar gir: ")
n2=input("2.Notunu gir: ")
while sayikontrol(n2)==False or int(n2)<0 or int(n2)>100:
    n2=input("2. Notunu yanlış girdin tekrar gir: ")
f=input("Final notunu gir: ")
while sayikontrol(f)==False or int(f)<0 or int(f)>100:
    f=input("Final notunu yanlış girdin, tekrar gir: ")
hesapla(n1,n2,f) 