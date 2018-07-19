class1 = []
class2 = []
class3 = []
errorflag=0
true=1
#-----------input data--------------------#
class1.append(input())
class1.append(int(input()))
class1.append(input())
if(class1[1]==2):
    class1.append(input())
class2.append(input())
class2.append(int(input()))
class2.append(input())
if(class2[1]==2):
    class2.append(input())
class3.append(input())
class3.append(int(input()))
class3.append(input())
if(class3[1]==2):
    class3.append(input())
#---------check class lenth-----------#
if(len(class1[0])!=4 or len(class2[0])!=4 or len(class3[0])!=4):
    errorflag=1
    true=0
#---------check hour-----------#
if(class1[1]<1 or class1[1]>2 or class2[1]<1 or class2[1]>2 or class2[1]<1 or class2[1]>2):
   errorflag=1
   true=0
#--------check sec date------------#
xsec1 = class1[2]
x1a,x1b=int(xsec1[0]),int(xsec1[1])
if(x1a>5 or x1a<1 or x1b<1 or x1b>8):
    errorflag=1
    true=0
if class1[1]==2:
    xsec2 = class1[3]
    x2a,x2b = int(xsec2[0]),int(xsec2[1])
    if(x2a>5 or x2a<1 or x2b<1 or x2b>8):
        errorflag=1
        true=0
ysec1 = class2[2]
y1a,y1b=int(ysec1[0]),int(ysec1[1])
if(y1a>5 or y1a<1 or y1b<1 or y1b>8):
    errorflag=1
    true=0
if class2[1]==2:
    ysec2 = class2[3]
    y2a,y2b=int(ysec2[0]),int(ysec2[1])
    if(y2a>5 or y2a<1 or y2b<1 or y2b>8):
        errorflag=1
        true=0
zsec1 = class3[2]
z1a,z1b=int(zsec1[0]),int(zsec1[1])
if(z1a>5 or z1a<1 or z1b<1 or z1b>8):
    errorflag=1
    true=0
if class3[1]==2:
    zsec2 = class3[3]
    z2a,z2b=int(zsec2[0]),int(zsec2[1])
    if(z2a>5 or z2a<1 or z2b<1 or z2b>8):
        errorflag=1
        true=0
#--------------------check collin-----------------------------
for i in range(2,len(class1)):
    for j in range(2,len(class2)):
        if(class1[i]==class2[j]):
            true=0
            print(class1[0],class2[0],class1[i],sep=",")
for i in range(2,len(class1)):
    for j in range(2,len(class3)):
        if(class1[i]==class3[j]):
            true=0
            print(class1[0],class3[0],class1[i],sep=",")
for i in range(2,len(class2)):
    for j in range(2,len(class3)):
        if(class2[i]==class3[j]):
            true=0
            print(class2[0],class3[0],class2[i],sep=",")
if(errorflag==1):
    print("-1")
if(true==1):
    print("correct")