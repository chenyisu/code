def turnLeft(lista,n):                                  #左轉
    newtest = [[0] *n for i in range(n)]                #陣列初始化                                  
    for i in range(n):
        for j in range(n):
            newtest[n-j-1][i] = lista[i][j]
    return newtest                                      #回傳旋轉後結果
def turnUpAndDown(lista,n):                             #上下翻轉
    newtest = [[0] *n for i in range(n)]                ##陣列初始化 
    newtest[:] = lista[::-1]
    return newtest                                      #回傳旋轉後結果
def turnRight(lista,n):                                 #右轉
    newtest = [[0] *n for i in range(n)]                #陣列初始化
    for i in range(n):
        for j in range(n):
            newtest[j][n-i-1] = lista[i][j]
    return newtest                                      #回傳旋轉後結果
def prinList(newtest,n):                                #印出最後結果
    for i in range(n):
        for j in range(n):
            print(newtest[i][j],sep="",end=" ")
        print()
def checkStatus(lista,turndata,n):                              #確認狀態
    for i in turndata:
        if(i=='L'):
            lista = turnLeft(lista,n)
        elif(i=='R'):
            lista = turnRight(lista,n)
        elif(i=='N'):
            lista = turnUpAndDown(lista,n)
        elif(i=='F'):
            prinList(lista,n)
def main():
    n = int(input())                            #輸入N值
    turndata = [i for i in input().split()]     #輸入 L R N旋轉
    data=1
    lista = [[] *n for i in range(n)]           #創建n*n矩陣                             #創建new n*n矩陣
    for i in range(n):
        for j in range(n):
            lista[i].append(data)
            data+=1
    checkStatus(lista,turndata,n)
main()