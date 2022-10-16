n=input()
v=list("aeiou")
for i in n:
    if i in v:
        v.remove(i)
if len(v)!=0:
    print(*v)
else:
    print(0)