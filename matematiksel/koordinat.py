def koordinatbul(y1,y2,x1,x2):
    m=(y1-y2)/(x1-x2)
    c=y1-x1
    print(f"""Verilen değerlerin karışığı:
          mx={m}x
          y={m}x+c
          c={c}
          sonuç={int(m)}x+{c}""")

x1=int(input("x1 koordinatını giriniz: "))
y1=int(input("y1 koordinatını giriniz: "))
x2=int(input("x2 koordinatını giriniz: "))
y2=int(input("y2 koordinatını giriniz: "))
koordinatbul(y1,y2,x1,x2)