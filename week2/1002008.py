def check(N):
    try: 
        N=int(N)
    except:
        return -2
    if(N==-1):
        return -1
    a1 = 1
    a2 = 1
    a3 = 0
    for i in range(N+1):
        if(i==1 or i==2):
            a3=1
        elif(i>2):
            a3=a1+a2
            a1=a2
            a2=a3
    return a3
while(True):
    N = check(input())
    if(N==-1):
        break
    elif(N<-1 or N==0):
        print("Error")
    else:
        print(N)