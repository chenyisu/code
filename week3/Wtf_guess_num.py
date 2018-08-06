def createShit():           #創造大便
    shit=[]
    for i in range(10000):  #範圍0-9999
        a = addzero(i)      #補足4位數(補0)
        if(ingnoreDouble(a)==True):     #檢查重複數字
            pass    #重複=略過
        elif(ingnoreDouble(a)==False):
            shit.append(a)          #不重複才加進大便LIST
    return shit     #回傳創造好的大便
def addzero(i):     #補0
    i=str(i)
    while(len(i)<4):
        i = "0"+ i
    return i
def ingnoreDouble(a):   #檢查重複數字
    for i in range(0,4):
        for j in range(i+1,4):
            if(a[i]==a[j]):
                return True
    return False
def checkAB(guess,bigShit):
    a,b=0,0
    for i in range(4):                  #猜測與答案幾A幾B
        if(bigShit[i]==guess[i]):
            a += 1
            b -= 1
        if(bigShit[i] in guess):
            b += 1
    if(a==abtemp[0] and b==abtemp[1]):
        return False
    else:
        return True
def checkShit(guess,bigShit):       #大便內元素比對猜測  是否與  猜測與答案  幾A幾B相同, 不相同將"index"存到待刪除LIST
    deltemp=[]
    for i in range(len(bigShit)):

        if(checkAB(guess,bigShit[i])==True):    #不相同將"index"存到待刪除LIST, 相同PASS.
            deltemp.append(i)
    return deltemp              
def main():
    bigShit = createShit()      #創建大便
    #print(len(bigShit))
    while(len(bigShit)>1):
        innput = [i for i in input().split(",")]        #輸入猜測答案 ,拆開
        guess=innput[0]         #取得猜測
        abtemp[0]=int(innput[1][0])     #取得A
        abtemp[1]=int(innput[1][2])     #取得B
        #print(abtemp)
        deltemp = checkShit(guess,bigShit)          #大便內元素比對猜測  是否與  猜測與答案  幾A幾B相同
        for i in reversed(deltemp):         #倒著POP刪除不要得可能
            bigShit.pop(i)
        #print(deltemp)
        #print(bigShit)
    print(bigShit[0])
    #print(bigShit)
abtemp=[-1,-1]
main()