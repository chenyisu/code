i = [int(i) for i in input().split()]
i.sort()
a,b,c = int(i[0]),int(i[1]),int(i[2])
def gettriangle(a,b,c):
    if(a+b<=c):
       print("1")
    elif(a==c):
        print("2")
    elif((a==b or b==c) and a**2+b**2>c**2):
        print("3")
    else:
        print("4")
    return

gettriangle(a,b,c)
