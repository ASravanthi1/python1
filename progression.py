N,A,D=map(int,input().split())
sum=0
for i in range(N):
    sum=sum+A
    A=A+D
    i=i+1
print (sum)
