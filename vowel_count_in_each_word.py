n=input()
v=list("aeiouAEIOU")
for i in n.split():
    c=0
    for j in i:
        if j in v:
            c+=1
    print(c,end=" ")
        