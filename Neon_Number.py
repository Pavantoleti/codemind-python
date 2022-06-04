num=int(input())
sqr=num*num
sumOfDigit=0
m=0
while sqr>0:
    sumOfDigit=sumOfDigit+sqr%10
    sqr=sqr//10
    m=sumOfDigit+sqr
if num==m:
    print("Neon Number")
else:
    print("Not Neon Number")