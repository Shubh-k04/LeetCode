a = [0,1,2,3,4]
b=[-1,2,3,3,2,4]
c=[15,14,13,12]
d=[-2,-4,13,9,8]
total = 24
count=0
for i in a:
    for j in b:
        for k in c:
            for l in d:
                sum=i+j+k+l
                if sum==total:
                    count+=1
print(count)
  
