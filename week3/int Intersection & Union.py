def selection(control):             #輸入功能SWITCH
    con = control[0]
    if(con==1):
        clearA()
    elif(con==2):
        clearB()
    elif(con==3):
        addA()
    elif(con==4):
        addB()
    elif(con==5):
        delA()
    elif(con==6):
        delB()
    elif(con==7):
       intersection()
    elif(con==8):
        union()
    elif(con==9):
        subcollection()
def clearA():                       #清除A
    setA.clear()
    printsetAB(setA,setB)
    return 0
def clearB():                       #清除B
    setB.clear()
    printsetAB(setA,setB)
    return 0
def addA():                         #新增元素至A
    if(control[1] not in setA):    
        setA.append(control[1])
    printsetAB(setA,setB)
    return 0
def addB():                         #新增元素至B

    if(control[1] not in setB): 
        setB.append(control[1])
    printsetAB(setA,setB)
    return 0
def delA():                         #從A刪除元素
    if(control[1] in setA):    
        setA.remove(control[1])
    printsetAB(setA,setB)
    return 0
def delB():                         #從B刪除元素
    if(control[1] in setB): 
        setB.remove(control[1])
    printsetAB(setA,setB)
    return 0
def intersection():                 #聯集(重複的不搬到TEMP)
    temp = []
    for i in range(len(setA)):
        temp.append(setA[i])
    for i in range(len(setB)):
        if(setB[i] not in setA):
            temp.append(setB[i])
    #temp.sort()
    #printintersection(list(set(temp)))
    printintersection(temp)

    return 0
def union():                        #交集
    temp =[]
    for i in range(len(setA)):
        for j in range(len(setB)):
            if(setA[i]==setB[j]):
                temp.append(setA[i])
    #temp.sort()
    #printintersection(list(set(temp)))
    printintersection(temp)
    return 0
def printsetAB(setA,setB):          #Print A & B(轉成字串配合輸出格式)
    print("A:",sep="",end="")
    StrA="" 
    for i in setA:
        StrA = StrA+str(i)+","
    print("[",StrA,"]",sep="",end="")

    print("B:",sep="",end="")
    StrB = ""
    for i in setB:
        StrB = StrB+str(i)+","
    print("[",StrB,"]",sep="")
    return 0
def printintersection(temp):        #Print TEMP(轉成字串配合輸出格式)
    strA=""
    for i in temp:
        strA = strA+str(i)+","
    print("[",strA,"]",sep="")
    return 0
def subcollection():                #判斷是否為子集合
    flag = 0
    for i in range(len(setA)):
            if(setA[i] in setB):
                flag +=1
    if(len(setA)==flag):
        print(1)
    else:
        print(0)
    return 0
setA = []*20
setB = []*20
while(True):
    control = [int(i) for i in input().split()]
    if(control[0]==0):
        break
    selection(control)
  