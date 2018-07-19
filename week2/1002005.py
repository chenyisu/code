B = int(input())
Num = int(input())
temp = []
if(2<=B<=9 and 0<=Num<=10000000):
    while(Num>=B):
        temp.append(Num%B)
        Num = Num//B
    temp.append(Num)
    for i in range(len(temp),0,-1):
        print(temp[i-1],sep="",end="")
else:
    print(-1)