import math
a = int(input())
b = int(input())
c = int(input())
X1 = ((-b)+math.sqrt(b*b-4*a*c))/(2*a)
X2 = ((-b)-math.sqrt(b*b-4*a*c))/(2*a)
print("%.1f"%X1)
print("%.1f"%X2)