def test():
    n,m,k = 5,2,4
    alist = [ i for i in range(1,n+1)]  #產生陣列,並賦值
    a = 0
    for i in range(k):
        a = (a+m-1)%len(alist)
        print(alist[a],end=" ")
        del alist[a]
        if a == len(alist):
            a = 0
    print(alist[a],end=" ")


def main():
    n,m,k = map(int,input().split())
    alist = [ i for i in range(1,n+1)]  #產生陣列,並賦值
    a = 0
    for i in range(k):
        a = (a+m-1)%len(alist)
        print(alist[a],end=" ")
        del alist[a]
        if a == len(alist):
            a = 0
    print(alist[a],end=" ")

#main()
test()