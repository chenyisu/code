from fractions import Fraction
Input = [int(i) for i in input().split()]
x1 = Input[0]
y1 = Input[1]
x2 = Input[2]
y2 = Input[3]
if(x1==x2):
    print("x=",x1,sep="")
elif(y1==y2):
    print("y=",y1,sep="")
else:
    m = (y1-y2)/(x1-x2)
    m1 = Fraction((y1-y2),(x1-x2))
    b = (x2*y1-x1*y2)/(x2-x1)
    b1 = Fraction((x2*y1-x1*y2),(x2-x1))

    print("y=",end="")
    if(m%1!=0):
        print("%.2fx"%m,end="")
    else:
        print(int(m),"x",end="",sep="")
    if(b>0):
        print("+",end="")
    if(b%1!=0):
        print("%.2fx"%b)
    else:
        print(int(b))
    print('y=',m1,"x",sep="",end="")
    if(b1>0): 
        print("+",end="")
    print(b1)
