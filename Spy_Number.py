n=int(input())
r=0
sum=0
mul=1
while(n>0):
    r=n%10
    n=n//10
    sum=sum+r
    mul=mul*r
if sum==mul:
    print("Spy Number")
else:
    print("Not Spy Number")