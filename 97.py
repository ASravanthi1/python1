mn=int(input())
rev=0
if mn<1000:
    while mn>0:
        rem=mn%10
        rev=(rev*10)+rem
        mn=mn//10
    print(rev)
