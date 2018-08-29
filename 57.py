mn,k=input().split()
mn,k=int(mn),int(k)
list=[int(x) for x in input().split()]
count=0
for i in range(0,mn):
    if k==list[i]:
        count+=1
print(count)
