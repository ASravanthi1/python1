m,n=map(int,input().split())
if m>n:
    sn=m
else:sn=n
while sn>0:
    if(sn%m==0) and (sn%n==0):
        c=sn
        break
    sn+=1
print(c)
