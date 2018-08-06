def check(list):            #檢查是否連成線
    winFlag = 0
    if(list[0]==0):
        if(list[1]==3 and list[2]==6):
            winFlag = 1
        elif(list[1]==1 and list[2]==2):
            winFlag = 1
        elif(list[1]==4 and list[2]==8):
            winFlag = 1
    elif(list[0]==1 and list[1]==4 and list[2]==7):
        winFlag = 1
    elif(list[0]==2):
        if(list[1]==4 and list[2]==6):
            winFlag = 1
        elif(list[1]==5 and list[2]==8):
            winFlag = 1
    elif(list[0]==3 and list[1]==4 and list[2]==5):
        winFlag = 1
    elif(list[0]==6 and list[1]==7 and list[2]==8):
        winFlag = 1

    return winFlag
def whoIsWinner(bingoPlayer1,bingoPlayer2,playNum,status):
    listP1=[]
    listP2=[]
    for i in range(3):
        a = bingoPlayer1.index(playNum[i])  #找出賓果數字在Player1的index
        b = bingoPlayer2.index(playNum[i])  #找出賓果數字在Player2的index
        listP1.append(a)    #將index存到陣列
        listP2.append(b)
    listP1.sort()   #並做排序
    listP2.sort()
    aP = check(listP1)  #檢查是否連成線並回傳 1 or 0
    bP = check(listP2)  #檢查是否連成線
    if(aP>bP):      #Player1 and Player2 比拚, 贏的存到結果陣列
        status.append(1)    #1  win
    elif(bP>aP):
        status.append(2)    #2  win
    else:
        status.append(0)    #0  draw
def pprint(status):
    for i in status:
        if(i==1):
            print("Player1 wins")
        elif(i==2):
            print("Player2 wins")
        elif(i==0):
            print("Draw")
def main():
    status=[]
    while(True):
        bingoPlayer1 = [i for i in input().split()] #第一筆輸入
        bingoPlayer2 = [i for i in input().split()] #第二筆輸入
        playNum = [i for i in input().split()]      #3個賓果數字
        flag = int(input())     #繼續 OR 結束 旗標
        whoIsWinner(bingoPlayer1,bingoPlayer2,playNum,status)
        if(flag==0):
            continue
        elif(flag==-1):
            pprint(status)
            break
main()