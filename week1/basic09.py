s = [int(i) for i in input().split()]
s.sort()
a=int(s[0])
if a+s[1]<=s[2] or s[0]<=0 or s[1]<=0 or s[2]<=0:
    print("Not Triangle")
elif s[0]**2+s[1]**2==s[2]**2:
    print("Right Triangle")
elif s[0]**2+s[1]**2<s[2]**2:
    print("Obtuse Triangle")
elif s[0]**2+s[1]**2>s[2]**2:
    print("Acute Triangle")
