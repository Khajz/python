def dikalan():
    a=int(input("Dikdörtgenin 1. kenarını giriniz!: "))
    b=int(input("Dikdörtgenin 2. kenarını giriniz!: "))
    alan=a*b
    cevre=(2*a)+(2*b)
    print(f"Kernarları {a} ve {b} olan dikdörtgenin alanı: {alan} ve çevresi: {cevre} !")
def ucalan():
    a=int(input("Üçgenin 1. kenarını giriniz!: "))
    b=int(input("Üçgennin 2. kenarını giriniz!: "))
    d=int(input("Üçgennin tabanını giriniz!: "))
    c=int(input("Üçgenin yüksekliğini giriniz!: "))
    alan=(d*c)/2
    cevre=a+b+d
    print(f"Kenarlar uzunlukları {a},{b},{d} ve yüksekliği {c} olan üçgenin alanı: {alan} ve çevresi: {cevre}")
def daialan():
    a=int(input("Dairenin yarıçapını giriniz!: "))
    alan=(a**2)*3.14
    cevre=(2*3.14)*a
    print(f"Yarıçapı {a} olan dairenin alanı: {alan} ve çevresi: {cevre}")

secim=input("""
Alan ve çevre hesaplayıcısına hoşgeldin!
    1.Dikdörtgen
    2.Üçgen
    3.Daire
    Seçim yap(1/2/3): """)

while True:
    if secim=='1':
        dikalan()
        break
    elif secim=='2':
        ucalan()
        break
    elif secim=='3':
        daialan()
        break
    else:
        secim=input("Yanlış seçim! Tekrar deneyiniz!: ")