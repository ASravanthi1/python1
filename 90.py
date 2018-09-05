mn=input()
k=[]
for i in range(0,len(mn)):
    if (mn[i]>='a' and mn[i]<='z') or (mn[i]>='A' and mn[i]<='Z'):
        c=0
    else:k.append(mn[i])
for j in range (0,len(k)):
    print(k[j],end='')
