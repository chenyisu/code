a,b = map(str,input().split('.'))
c,d = map(str,input().split('.'))
N = int(input())
if(N>60):
    print("Error")
    exit
def add(a,b,c,d,N):
    a,c = int(a),int(c)
    ac = (a+c)
    if(len(b)>len(d)):
        point = len(b)
        d = int(d)*(10**(point-len(d)))
        b = int(b)
    elif(len(d)>len(b)):
        point = len(d)
        b = int(b)*(10**(point-len(b)))
        d = int(d)
    b,d = int(b),int(d)
    bd = (b+d)
    if(bd>=10**point):
        ac = ac + (bd//10**point)
        bd = bd%10**point
    bd = str(bd)
    if(point<N):
        blist = list(bd)
        for i in range(N-point):
            blist.append('0')
        bdtemp=""
        for i in blist:
            bdtemp += i
        print(ac,".",bdtemp,sep="")
    else:
        print(ac,".",bd[0:N],sep="")
def sub(a,b,c,d,N):
    a,c = int(a),int(c)
    ac = (a-c)
    if(len(b)>len(d)):
        point = len(b)
        d = int(d)*(10**(point-len(d)))
        b = int(b)
    elif(len(d)>len(b)):
        point = len(d)
        b = int(b)*(10**(point-len(b)))
        d = int(d)
    b,d = int(b),int(d)
    bd = (b-d)
    if(bd<0):
        bd = bd+10**(point-1)
        ac -= 1
    bd = str(bd)
    print(ac,".",bd[0:N],sep="")

def times(a,b,c,d,N):
    point = len(b)+len(d)
    line1 = a+b
    line2 = c+d
    ans = int(line1) * int(line2)
    ans = str(ans)
    alist = list(ans)
    alist.reverse()
    alist.insert(point,'.')
    alist.reverse()
    temp=""
    for i in range(len(alist)):
        temp = temp+alist[i]
    temp = temp.split(".")
    a,b = temp[0],temp[1]
    print(a,".",b[0:N],sep="")
        

    
add(a,b,c,d,N)
sub(a,b,c,d,N)
times(a,b,c,d,N)