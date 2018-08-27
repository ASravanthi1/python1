n=int(input(""))
a=0
b=1
count=0
if(n==0):
    print(a)
elif(n<0):
    print("negative number")
else:
    while(count<n):
        print(a,sep=' ',end=' ')
        nexterm=a+b
        a=b
        b=nexterm
        count+=1
