mn=input()
count=0
count1=0
for i in range(0,len(mn)):
    if ((mn[i]>='a') and (mn[i]<='z') or (mn[i]>'A') and (mn[i]<'Z')):
        count=1
    elif((mn[i]=='1' or mn[i]=='2' or mn[i]=='3' or mn[i]=='4' or mn[i]=='5' or mn[i]=='6' or mn[i]=='7' or mn[i]=='8' or mn[i]=='9' or mn[i]=='0')):
         count1=1
if count+count1==2:
    print("Yes")
else:print("No")
