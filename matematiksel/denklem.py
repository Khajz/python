def kokbul(a,b,c):
    kok1=(-b-(((b**2)-4*a*c)**(1/2)))/(2*a)
    kok2=(-b+(((b**2)-4*a*c)**(1/2)))/(2*a)
    print(f"{a}x^2+{b}x+{c} denkleminin kökleri: {kok1} ve {kok2}")

a=int(input("ax^2+bx+c denklemindeki a değerini yazınız: "))
b=int(input("ax^2+bx+c denklemindeki b değerini yazınız: "))
c=int(input("ax^2+bx+c denklemindeki c değerini yazınız: "))

kokbul(a,b,c)