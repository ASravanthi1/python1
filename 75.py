mn=list(input())
f=len(mn)
kk=len(mn)/2
k=int(len(mn)/2)
if f%2==0:
    mn[k-1]="*"
    mn[k]="*"
else:mn[k]="*"
for i in range(0,len(mn)):
    print(mn[i],end='')
