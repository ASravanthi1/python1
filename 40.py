n=int(input(""))
a=1
b=1
count=0
c=0
k=" "
if(n==0):
    print(a)
elif(n<0):
    print("negative number")
else:
    while(count<n):
        if(c==0):
            print(a,end="")
        else:
            print("",end=k)
            print(a,end="")
        nexterm=a+b
        a=b
        b=nexterm
        count+=1
        c+=1
