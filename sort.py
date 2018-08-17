s=int(input())
list=[int(x) for x in input().split()]
list.sort()
print (" ".join(map(str,list)))
