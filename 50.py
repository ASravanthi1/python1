n=int(input(""))
i=1
while True:
    if(2**i<=n):
        if(2**i==n):
            print("yes")
            break
    else:
        print("no")
        break
    i=i+1
