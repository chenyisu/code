N = int(input())        #輸入幾筆購買資料
dict={}     #創字典
for i in range(N):      #LOOP N筆
    inputt = [int(i) for i in input().split(",")]
    inputt.sort()   #輸入後排序
    for i in range(len(inputt)):
        for j in range(i+1,len(inputt)):    #2樣商品比對
            d = (int(inputt[i]),int(inputt[j])) #創建KEY值
            if(d in dict):      #如已在字典中
                dict[d] = dict[d] + 1   #Value ++
            else:
                dict[d]=1       #不在字典中-->創建並初始1
    maxitem = max(dict,key=dict.get)    #找出最大Value並取得key
print(maxitem[0],maxitem[1],dict[maxitem],sep=",")  #印出key值 And 對應Value