ab=int(input())
s,s1=input().split()
s,s1=int(s),int(s1)
if(ab>s and ab<s1) or (ab>s1 and ab<s):
    print("yes")
else:print("no")
