mn=input()
ch=[]
for i in range(0,len(mn)):
    ch.append(mn[i])
k=[]
i=len(mn)-1
count=0
while i>=0:
    k.append(mn[i])
    i-=1
for i in range(0,len(ch)):
    if ch[i]==k[i]:
        count+=1
if count==len(ch):
    print("yes")
else:print("no")
