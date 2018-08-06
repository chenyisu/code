def cal(lista):         #文字轉字串,並算出總合
    result = 0
    for i in range(9):
        a = int(lista[i])
        result += a
    return result
lista = []      #新LIST
for i in range(9):
    lista.append(input())   #輸入DATA
for i in range(9):          #掃描  找"0"
    for j in range(9):
        if(lista[i][j]=='0'):
            ans = cal(lista[i])
            ans = 45-ans    #數獨規則 1-9,  即45-總和 = 缺少的數字
            print(i,j,ans)
