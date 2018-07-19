summ = 0
flag = 0
for i in range(4):
    if(flag==1):
        flag=0
        continue
    a = int(input())
    summ += a
    if(a==10 and i<2):
        flag = 1
print(summ)