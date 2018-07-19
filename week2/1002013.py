from fractions import Fraction
def check0(aFraction):
    for i in range(2):
        if(aFraction[i]==0):
            aFraction[0]=-0.1
aFraction = [int(i) for i in input().split("/")]
bFraction = [int(i) for i in input().split("/")]
check0(aFraction)
check0(bFraction)

if(aFraction[0]==-0.1 or bFraction[0]==-0.1):
    print("ERROR")
    print("ERROR")
else:
    a = Fraction(aFraction[0],aFraction[1])
    b = Fraction(bFraction[0],bFraction[1])
    c = a+b
    cint = int(c)
    d = a*b
    if(cint>0 and c-cint==0):
        print(cint)
    elif(cint<0 and c-cint==0):
        print(cint)
    elif(cint>0 and c-cint!=0):
        print(cint,"(",c-cint,")",sep="")
    elif(cint<0 and c-cint!=0):
        print(cint,"(",abs(c-cint),")",sep="")
    else:
        print(c)
    print(d)
