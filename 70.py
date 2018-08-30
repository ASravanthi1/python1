ab=int(input())
i=0
while i<1000:
    if ab<2**i:
        print(2**i)
        break
    i+=1
