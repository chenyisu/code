bb = []
summ = 0
for i in range(21):
    bb.append(int(input()))
    summ += bb[i]
for i in range(0,18,2):
    if(bb[i]+bb[i+1]==10 and bb[i+1]!=0):
        summ += bb[i+2]
    elif(bb[i]==10 and bb[i+1]==0):
        summ += bb[i+2] + bb[i+3]
print(summ)