mn=int(input())
if(mn<=1000):
    storage=input()
    storage=[int(x) for x in storage.split()]
    kk=sorted(storage[0:mn])
for i in range(0,mn):
    if(i<mn-1):
        f=' '
    else:
        f=''
    print(kk[i],end=f)

