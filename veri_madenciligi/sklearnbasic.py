import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x= [6, 9, 12, 12, 15, 21, 24, 24, 27, 30, 36, 39, 45, 48, 57, 60] 

y = [12, 18, 30, 42, 48, 78, 90, 96, 96, 90, 84, 78, 66, 54, 36, 24]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(1, 60, 100)


print(r2_score(y,mymodel(x)))

print(f"X=8 için : {mymodel(8)}")
print(f"X=25 için : {mymodel(25)}")
print(f"X=49 için : {mymodel(49)}")

plt.scatter(x, y)
plt.plot(myline, mymodel(myline),color="purple",linewidth = "2.5")
plt.show()