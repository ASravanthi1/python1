v=int(input())
count=0
sum=0
while v>0:
    rem=v%10
    sum=sum+rem
    v=v//10
print(sum)
