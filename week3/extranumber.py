
def change(num):              #輸入資料到陣列  反轉
    temp=[]
    for i in num:
        temp.append(int(i))
    temp.reverse()
    return temp
def paddingZero(num1,num2):     #補零到一樣長度
    distance = len(num1)-len(num2)
    if(distance>0):
        for i in range(distance):
            num2.append(0)
        return num2
    elif(distance<0):
        distance = abs(distance)
        for i in range(distance):
            num1.append(0)
        return num1
def add(num1,num2):         #相加
    carry = 0
    ans=[]
    for i in range(len(num1)):
        cal = num1[i]+num2[i]+carry
        if(cal>=10):
            carry=1
            cal -= 10
        else:
            carry=0
        ans.append(cal)
    if(carry==1):
        ans.append(carry)
    ans.reverse()
    return ans
def sub(num1,num2):     #相減
    carry = 0
    ans=[]
    for i in range(len(num1)):
        cal = num1[i]-num2[i]+carry
        if(cal<0):
            carry=-1
            cal += 10
        else:
            carry=0
        ans.append(cal)
    if(carry==1):
        ans.append(carry)
    ans.reverse()
    ans = delzero(ans)
    if(len(ans)==0):
        print(0)
    return ans
def delzero(ans):       #刪除過多得0
    for i in range(len(ans)):
        if(ans[0]==0):
            del (ans[0])
    return ans
def muti(num1,num2):        #相乘法
    temp = [0]*120
    for i in range(len(num1)):
        for j in range(len(num2)):
            cal = num1[i]*num2[j]
            if(i+j==0):
                temp[i+j]=cal
            else:
                temp[i+j] += cal
    adjust(temp)
    temp.reverse()
    delzero(temp)
    return temp
def adjust(temp):           #相乘後處理進位
    for i in range(len(temp)):
        if(temp[i]>=10):
            carry = temp[i] // 10
            temp[i+1] = temp[i+1] + carry
            temp[i] = temp[i] - (carry*10)
    return temp
def printresult(a):         #print
    for i in range(len(a)):
        print(a[i],end='')
    print()
        
def main():
    num1 = change(input())
    num2 = change(input())
    paddingZero(num1,num2)
    printresult(add(num1,num2))
    printresult(sub(num1,num2))
    printresult(muti(num1,num2))

main()