i = [int(i) for i in input().split()]
a,b,c,d,e = int(i[0]),int(i[1]),int(i[2]),int(i[3]),int(i[4])
total = a+b+c+d+e
avg = total/5
dif = ((a-avg)**2 + (b-avg)**2 + (c-avg)**2 + (d-avg)**2 + (e-avg)**2) / 5
dig = int((dif**0.5)*100)/100
print("%.2f"%avg)
print("%.2f"%dif)
print("%.2f"%dig)