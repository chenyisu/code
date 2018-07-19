x = int(input())
y = int(input())
z = int(input())
total = 0
if x>0 and x<=10:
    total += x*380
elif x>10 and x<=20:
    total += x*380*0.9
elif x>20 and x<=30:
    total += x*380*0.85
elif x>31:
    total += x*380*0.8

if y>0 and y<=10:
    total += y*1200
elif y>10 and y<=20:
    total += y*1200*0.95
elif y>20 and y<=30:
    total += y*1200*0.85
elif y>31:
    total += y*1200*0.8

if z>0 and z<=10:
    total += z*180
elif z>10 and z<=20:
    total += z*180*0.85
elif z>20 and z<=30:
    total += z*180*0.8
elif z>31:
    total += z*180*0.7

print(int(total))