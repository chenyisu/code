def pprint(word2,diction):
    for i in word2:
        print(i,end=" ")
    print()
    print(len(word2))
    for i in range(len(diction)):
        if(diction[i][1]!=0):
            print(diction[i][0],diction[i][1],end=" ")
            print()

def main():
    diction=[]
    while(True):    #無限迴圈直到-1
        word = input()  #輸入
        delist=[]   
        if(word=='-1'): #結束
            word2 = [i for i in input().split()]        #輸入英文句子
            for i in range(len(word2)):
                for j in range(len(diction)):
                    if(word2[i]==diction[j][0]):
                        diction[j][1] += 1
                        delist.append(i)
            diction.sort(key=lambda x:(x[0].lower(),x[1]))
            for i in reversed(delist):
                word2.pop(i)
            pprint(word2,diction)
            break
        diction.append([word,0])
        #diction.append([0,len(word),word])
 
    
main()

#diction.sort(key=lambda x:(x[0].lower(),x[1]))
