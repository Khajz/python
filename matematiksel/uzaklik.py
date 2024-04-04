def mesafebul(y1,y2,x1,x2):
    a=(x2-x1)**2
    b=(y2-y1)**2
    c=(a+b)**(1/2)
    print(round(c,2))

x1=int(input("x1 koordinatını giriniz: "))
y1=int(input("y1 koordinatını giriniz: "))
x2=int(input("x2 koordinatını giriniz: "))
y2=int(input("y2 koordinatını giriniz: "))
mesafebul(y1,y2,x1,x2)