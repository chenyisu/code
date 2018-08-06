def count(temp):
    pause = []               #判斷重複牌出現幾次
    for i in range(len(temp)):
        pause.append(temp.count(temp[i]))
    pause.sort()
    temp.sort()
    reconize(pause,temp)
def reconize(pause,temp):
    if(pause[4]==4):
        print("5")                  #Four of a kind鐵支
    elif(pause[4]==3 and pause[0]==2):
        print("4")                  #Full House 葫蘆
    elif(pause[4]==3 and pause[0]==1):
        print("3")                  #Three of a kind 三條
    elif(pause[4]==2 and pause[1]==2):
        print("2")                  #Two Pair  
    elif(pause[4]==2 and pause[1]==1):
        print("1")                  #Pair
    elif(pause[4]==1 and pause[1]==1):  #判斷是否沒重複
        if(temp[4]-temp[0]==4 or (temp[4]==13 and temp[3]-temp[0]==3)):  #判斷是否為順子
            if(len(one)==5 or len(two)==5 or len(the)==5 or len(fou)==5): #判斷是否同花色
                print("7")      #同花順
            else:
                print("6")      #順子
        else:
            print("0")              #單張
def selectC(c,temp):
        if(c==0):                   #分別丟到各花色
            one.append(temp)
        elif(c==1):                 #分別丟到各花色
            two.append(temp)     
        elif(c==2):                 #分別丟到各花色
            the.append(temp)     
        elif(c==3):                 #分別丟到各花色
            fou.append(temp) 
def keyin(temp):
    inputpoke = [(i) for i in input().split()]  #輸入
    for i in range(len(inputpoke)):             #整理輸入值,分開數字與花色
        a = int(inputpoke[i][0])
        b = int(inputpoke[i][1])
        if(len(inputpoke[i])>2):
            c = int(inputpoke[i][2])
            temp.append((a*10)+b)
        elif(len(inputpoke[i])<=2):
            temp.append(a)
            c = b
        if(c<0 or c>3):             #確認花色編碼是否錯誤
            print("error")
            break  
        else:
            selectC(c,temp[i])      #丟到各花色
    count(temp)
def main():
    temp=[]
    keyin(temp)
one=[]
two=[]
the=[]
fou=[]
main()