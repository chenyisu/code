import math
a = int(input())
b = int(input())
c = int(input())
T = ((b*b)-(4*a*c))
if(T>=0):
    T = int((math.sqrt(T))*10)/10
    X1 = int(((-b+T)/(2*a))*10)/10
    X2 = int(((-b+T)/(2*a))*10)/10
    print(X1)
    print(X2)
elif(T<0):
    T = abs(T)
    T = int((math.sqrt(T))*10)/10
    X1 = int(((-b)/(2*a))*10)/10
    i = int(((T)/(2*a))*10)/10
    if(i>=0):
        print("%.1f+%.1fi"%(X1,i))
        print("%.1f-%.1fi"%(X1,i))
    else:
        i = abs(i)
        print("%.1f-%.1fi"%(X1,i))
        print("%.1f+%.1fi"%(X1,i))

