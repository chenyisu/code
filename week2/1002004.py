height = int(input())
N_1 = height//2+1
for i in range(N_1):
    for k in range(i+1,N_1):
        print(".",sep="",end="")
    for j in range(2*i+1):
        print("*",sep="",end="")
    for k in range(i,N_1-1):
        print(".",sep="",end="")
    print()
for i in range(N_1-1,0,-1):
    for k in range(N_1,i,-1):
        print(".",sep="",end="")
    for j in range(1,2*i):
        print("*",sep="",end="")
    for k in range(N_1,i,-1):
        print(".",sep="",end="")    
    print()
