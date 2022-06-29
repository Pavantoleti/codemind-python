a=input()
vo=["a","e","i","o","u","A","E","I","O","U"]
vou=con=dig=sp=0
for i in a:
    if i.isdigit():
        dig+=1
    elif i==" ":
        sp+=1
    elif i in vo:
        vou+=1
    else:
        con+=1
print("Vowels:",vou)
print("Consonants:",con)
print("Digits:",dig)
print("White spaces:",sp)