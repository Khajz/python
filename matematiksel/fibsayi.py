fiblist=[]
fiblist.append(1)
fiblist.append(1)
for i in range(2,100):
    fiblist.append(fiblist[i-2]+fiblist[i-1])
print(fiblist)