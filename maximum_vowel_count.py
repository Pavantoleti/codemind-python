s=list(input().lower().split(" "))
d={}
v="aeiou"
for i in s:
    c=0
    for j in i:
        if j in v:
            c+=1
    d[c]=i
print(max(d))
