a={}
b = [1,2,3]
for i in b:
    a.get(i,0)
    a[i]+=1
print(a)