tri = int(input())
a = int(input())
aa = (a//2)+1
#--------------------input 1 -------------------
def LeftTrianlge(aa):
    for i in range(1,aa+1):
        for j in range(1,i+1):
            print(j,sep="",end="")
        print()
    for i in range(aa,1,-1):
        for j in range(1,i):
            print(j,sep="",end="")
        print()
#-------------------input 2----------------------
def RightTriangle(aa):
    for i in range(1,aa+1):
        for k in range(aa,i,-1):
            print(".",sep="",end="")
        for j in range(i,0,-1):
            print(j,sep="",end="")
        print()
    for i in range(aa-1,0,-1):
        for k in range(aa,i,-1):
            print(".",sep="",end="")
        for j in range(i,0,-1):
            print(j,sep="",end="")
        print()
#-------------------------------------------------
if(tri==1):
    LeftTrianlge(aa)
elif(tri==2):
    RightTriangle(aa)
