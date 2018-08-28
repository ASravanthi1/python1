mn,lm=input().split()
mn=int(mn)
lm=int(lm)

for i in range(mn+1,lm):
    count=0
    for j in range(1,i):
        if(i % j) == 0:
            count+=1
            if(count == 2):
                break
    else:
        if(j < mn+200):
           k=' '
        else:
            k=''
        print(j+1,end=k)

