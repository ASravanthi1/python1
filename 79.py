a,b=input().split()
a,b=int(a),int(b)
pro=a*b
count=0
for i in range(0,pro):
    if i*i==pro:
        count=1
if count==1:
    print("yes")
else:print("no")
