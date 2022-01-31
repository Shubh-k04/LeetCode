a={}
res = []
b = [1,2,3,2]
c = [0,1,2,2]
for i in b:
    a[i]=a.get(i,0)+1
    
print(a)
for j in c:
    if (j in a) and (a[j]>0):
        a[j]-=1
        res.append(j)
print(res)