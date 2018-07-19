aa = [0]*40
mid = 20
bb = []
n = int(input())
for i in range(n):
    bb.append([int(input()),int(input())])
    bb[i].sort()
    for j in range(bb[i][0]+mid,bb[i][1]+mid):
        aa[j] = 1
print(sum(aa))