ab=int(input())
for i in range(1,ab+1):
    if(ab%i==0):
        if i<ab:
            k=' '
        else:
            k=''
        print(i,end=k)
