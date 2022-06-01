a,b,c=map(int,input().split())
import math
s=(a+b+c)/2
p=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("%0.2f"%p)