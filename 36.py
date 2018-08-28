mn=input()
b=sum(c.isalpha() for c in mn)
d=sum(c.isdigit() for c in mn)
f=sum(c.isspace() for c in mn)
spsymbl=len(mn)-b-d-f
print(spsymbl)
