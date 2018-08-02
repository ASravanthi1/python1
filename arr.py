N,K=input().split()
N,K=int(N),int(K)
sum=0
list=[int(x) for x in input().split()]
for i in range(0,K):
    sum=sum+list[i]
print(sum)
