mn=input()
evn=""
odd=""
for i in range(0,len(mn)):
    if (i)%2==0:
        evn=evn+(mn[i])
    else:
        odd=odd+(mn[i])
print(evn,odd)
