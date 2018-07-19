
def checkTrans(inputdata):
    try:
        N = float(inputdata[0])
        C = float(inputdata[1])
        W = int(inputdata[2])
    except:
        return 999
    if(N<-100 or N>0 or ((N*10)%1!=0)):
        return 999
    if(C<0 or C>30000 or ((N*10)%1!=0)):
        return 999
    if(W<0 or W>10000 or (W%1)!=0):
        return 999
    pokeMon(N,C,W)
    
def pokeMon(N,C,W):
    evo = 0
    W_cla = W
    while(C>=abs(N) and W>=1 and evo<W):
        C = C+N+1.5
        evo += 1
        print(C,"1")
        if(W==0 or ((W*1.5)+C)<N):
            break
        while(C<abs(N) and W>=1):
            W -= 1
            C += 1.5
            print(C,"2")
    print(evo)
    print(C)


inputdata =[i for i in input().split()]
N = checkTrans(inputdata)
if(N==999):
    print("error")



