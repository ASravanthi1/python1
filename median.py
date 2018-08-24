s=int(input(""))
lst=[int(x) for x in input().split()]
s1=0
for i in range(0,s):
    s1+=lst[i]
print(int(s1/s))
