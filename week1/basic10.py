#---------------input data-----------
flag_error = 0
true = 0
xid = input()
xhour = int(input())
class1=set()
if(xhour==2):
    xsec1 = input()
    xsec2 = input()
    class1.add(xsec2)
    class1.add(xsec1)
else:
    xsec1 = input()
    class1.add(xsec1)
yid = input()
yhour = int(input())
class2=set()
if(yhour==2):
    ysec1 = input()
    ysec2 = input()
    class2.add(ysec2)
    class2.add(ysec1)
else:
    ysec1 = input()
    class2.add(ysec1)
zid = input()
zhour = int(input())
class3=set()
if(zhour==2):
    zsec1 = input()
    zsec2 = input()
    class3.add(zsec2)
    class3.add(zsec1)
else:
    zsec1 = input()
    class3.add(zsec1)
#---------------check class and hours-----------
if(len(xid)!=4 or len(yid)!=4 or len(zid)!=4):
    flag_error = 1
    true = 1
if(xhour>2 or yhour>2 or zhour>2 or xhour<0 or yhour<0 or zhour<0):
    flag_error = 1
    true = 1
#---------------check date and class number-----------
if(int(xsec1[0])>5 or int(xsec1[0])<=0 or int(xsec1[1])>8 or int(xsec1[1])<=0
or int(ysec1[0])>5 or int(ysec1[0])<=0 or int(ysec1[1])>8 or int(ysec1[1])<=0
or int(zsec1[0])>5 or int(zsec1[0])<=0 or int(zsec1[1])>8 or int(zsec1[1])<=0):
    flag_error = 1
    true = 1

if(xhour==2):
    if(int(xsec2[0])>5 or int(xsec2[0])<=0 or int(xsec2[1])>8 or int(xsec2[1])<=0):
        flag_error = 1
        true = 1
if(yhour==2):
    if(int(ysec2[0])>5 or int(ysec2[0])<=0 or int(ysec2[1])>8 or int(ysec2[1])<=0):
        flag_error = 1
        true = 1
if(zhour==2):
    if(int(zsec2[0])>5 or int(zsec2[0])<=0 or int(zsec2[1])>8 or int(zsec2[1])<=0):
        flag_error = 1
        true = 1

#----------------------collin--------------------------1
if(flag_error !=1):
    if(len(class1&class2)==2):
        true = 1
        flag1 = (class1&class2)
        flag1_2 = (class1&class2).pop()
        for i in flag1:
            flag1_1 =i
        print(xid,yid,flag1_1,sep=",")
        print(xid,yid,flag1_2,sep=",")
    elif(len(class1&class2)==1):
        true = 1
        flag1_1 = (class1&class2).pop()
        if(flag1_1!=0):
            print(xid,yid,flag1_1,sep=",")
#--------------------------------------------1
if(flag_error !=1):
    if(len(class1&class3)==2):
        true = 1
        flag2 = (class1&class3)
        flag2_2 = (class1&class3).pop()
        for i in flag2:
            flag2_1 =i
        print(xid,zid,flag2_1,sep=",")
        print(xid,zid,flag2_2,sep=",")
    elif(len(class1&class3)==1):
        true = 1
        flag2_1 = (class1&class3).pop()
        if(flag2_1!=0):
            print(xid,zid,flag2_1,sep=",")
#---------------------------------------------
if(flag_error !=1):
    if(len(class2&class3)==2):
        true = 1
        flag3 = (class2&class3)
        flag3_2 = (class2&class3).pop()
        for i in flag3:
            flag3_1 =i
        print(yid,zid,flag3_1,sep=",")
        print(yid,zid,flag3_2,sep=",")
    elif(len(class2&class3)==1):
        true = 1
        flag3_1 = (class2&class3).pop()
        if(flag3_1!=0):
            print(yid,zid,flag3_1,sep=",")
#--------true or false--------------
if(flag_error==1):
    print(-1)
elif(true == 0):
    print("correct")