
def CheckError(y):
    pointflag = 0
    minflag = 0
    if(y[0]=="." or (y[0]=='0' and len(y)>1) or len(y)>8 or (y[0]=='-' and y[1]=='0')):
        return -1
    for i in range(len(y)):
        if(y[i]=="%" or y[i]=="$" or y[i]=="e" or(y[i]=="."and y[i+1]=="-")):
            return -1
        if(y[i]=="."):
            pointflag += 1
        if(y[i]=="-"):
            minflag += 1
            if(pointflag>1 or minflag>1):
                return -1
                
def Check5Function(x):
    if(2<=x[0] and x[0]<=1000 and len(x)==1):
        return x[0]
    elif((x[0]==0 or x[0]==1) and len(x)==1):
        return 1000
    elif(x[0]<0 and len(x)==1):
        return x[0]*(-11)
    elif(len(x)!=1 and x[0]>0):
        return x[0]
    elif(len(x)!=1 and x[0]<0):
        return x[1]
    else:
        return -1
    
y = input()
n = CheckError(y)
if(n==-1):
    print("error")
else:
    maxprime = 2
    ab = [int(i) for i in y.split(".")]
    n = Check5Function(ab)
    for i in range(2,n+1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            maxprime = i
    print(maxprime)
