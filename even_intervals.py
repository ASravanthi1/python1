a,b=input().split()
a,b=int(a),int(b)
count=0
for i in range(a+1,b):
    
    if(i%2==0):
        if i<b-2:
            k=" "
        else:k=""
        print(i,end=k)
    
