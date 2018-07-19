a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
lenline = 0
lenline += abs(a-b)
if(c<=b and d>b):
    lenline += abs(b-d)
elif(c>b):
    lenline += abs(c-d)
if(e<=d and f>d):
    lenline += abs(d-f)
if(e>d):
    lenline += abs(e-f)
print(lenline)