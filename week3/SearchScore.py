class student():
    def __init__(self,num,csScore,pgScore):
        self.num = num
        self.csScore = csScore
        self.pgScore = pgScore
        self.avg = (csScore+pgScore)//2
    def getNum(self):
        return self.num
    def getCsScore(self):
        return self.csScore
    def getPgScore(self):
        return self.pgScore
    def getAvg(self):
        return self.avg

def toLoop1(students,whichNum):
    for i in students:
        if(i.num==whichNum):
            return i
def toLoop2(students,maxtemp):
    for i in students:
        if(i.getAvg()>maxtemp[0]):
            maxtemp[0] = i.getAvg()
        if(i.getCsScore()>maxtemp[1]):
            maxtemp[1] = i.getCsScore()
        if(i.getPgScore()>maxtemp[2]):
            maxtemp[2] = i.getPgScore()
    return maxtemp
def toLoop3(students,mintemp):
    for i in students:
        if(i.avg<mintemp[0]):
            mintemp[0] = i.avg
        if(i.csScore<mintemp[1]):
            mintemp[1] = i.csScore
        if(i.pgScore<mintemp[2]):
            mintemp[2] = i.pgScore
    return mintemp
def toLoop4(students,functionNum,select):
    ab = sorted(students,key=lambda x:x.getNum())
    for i in ab:
        if(i.getAvg()<60 and functionNum==1 and select==4):
            print(i.getNum(),":",i.getAvg(),sep="")
        elif(i.getCsScore()<60 and functionNum==2 and select==4):
            print(i.getNum(),":",i.getCsScore(),sep="")
        elif(i.getPgScore()<60 and functionNum==3 and select==4):
            print(i.getNum(),":",i.getPgScore(),sep="")
        
        elif(i.getAvg()>60 and functionNum==1 and select==5):
            print(i.getNum(),":",i.getAvg(),sep="")
        elif(i.getCsScore()>60 and functionNum==2 and select==5):
            print(i.getNum(),":",i.getCsScore(),sep="")
        elif(i.getPgScore()>60 and functionNum==3 and select==5):
            print(i.getNum(),":",i.getPgScore(),sep="")
def toLoop5(students,functionNum):
    if(functionNum==1):
        sortAvg = sorted(students,key=lambda x:x.getAvg(),reverse=True)
        print("1st",":",sortAvg[0].getNum()," ",sortAvg[0].getAvg(),sep="")
        print("2nd",":",sortAvg[1].getNum()," ",sortAvg[1].getAvg(),sep="")
        print("3rd",":",sortAvg[2].getNum()," ",sortAvg[2].getAvg(),sep="")
    elif(functionNum==2):
        sortcs = sorted(students,key=lambda x:x.getCsScore(),reverse=True)
        print("1st",":",sortcs[0].getNum()," ",sortcs[0].getCsScore(),sep="")
        print("2nd",":",sortcs[1].getNum()," ",sortcs[1].getCsScore(),sep="")
        print("3rd",":",sortcs[2].getNum()," ",sortcs[2].getCsScore(),sep="")
    elif(functionNum==3):
        sortpg = sorted(students,key=lambda x:x.getPgScore(),reverse=True)
        print("1st",":",sortpg[0].getNum()," ",sortpg[0].getPgScore(),sep="")
        print("2nd",":",sortpg[1].getNum()," ",sortpg[1].getPgScore(),sep="")
        print("3rd",":",sortpg[2].getNum()," ",sortpg[2].getPgScore(),sep="")        
def functionOne(students,functionNum):
    whichNum = input()
    if(functionNum==1):
        i = toLoop1(students,whichNum)
        print(i.avg)
    elif(functionNum==2):
        i = toLoop1(students,whichNum)
        print(i.csScore)
    elif(functionNum==3):
        i = toLoop1(students,whichNum)
        print(i.pgScore)
def functionTwo(students,functionNum):
    maxtemp=[0]*3
    maxtemp = toLoop2(students,maxtemp)
    maxAvg = maxtemp[0]
    maxcsScore = maxtemp[1]
    maxpgScore = maxtemp[2]
    if(functionNum==1):
        print(maxAvg)
    elif(functionNum==2):
        print(maxcsScore)
    elif(functionNum==3):
        print(maxpgScore)
def functionThree(students,functionNum):
    mintemp=[101]*3
    mintemp = toLoop3(students,mintemp)
    minAvg = mintemp[0]
    mincsScore = mintemp[1]
    minpgScore = mintemp[2]
    if(functionNum==1):
        print(minAvg)
    elif(functionNum==2):
        print(mincsScore)
    elif(functionNum==3):
        print(minpgScore)
def functionFour(students,functionNum,select):
    toLoop4(students,functionNum,select)
def functionFive(students,functionNum,select):
    toLoop4(students,functionNum,select)
def functionSix(students,functionNum):
    toLoop5(students,functionNum)
def selectFunction(students):
    select = int(input())
    functionNum = int(input())
    if(select==1):
        functionOne(students,functionNum)
    elif(select==2):
        functionTwo(students,functionNum)
    elif(select==3):
        functionThree(students,functionNum)
    elif(select==4):
        functionFour(students,functionNum,select)
    elif(select==5):
        functionFive(students,functionNum,select)
    elif(select==6):
        functionSix(students,functionNum)
def main():
    students =[]
    while(True):
        s=input()
        if(s=='-1'):
            selectFunction(students)
            break
        num,csScore,pgScore = map(str,s.split(' '))
        csScore = int(csScore)
        pgScore = int(pgScore)
        students.append(student(num,csScore,pgScore))

main()