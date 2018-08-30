a=input()
count=0
for i in range(0,len(a)):
    if(a[i]=='0' or a[i]=='1'):
        count+=1
if count==len(a):
    print("yes")
else:print("no")
