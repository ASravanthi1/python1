m,n=map(int,input().split())
if m>n:
    sn=m
else:sn=n
for i in range(1,sn+1):
    if(n%i==0) and (m%i==0):
        c=i
print(c)
