max_line = 0
max_area = 0
while(True):
    n = [int(i) for i in input().split(" ")]
    if(n[0]==-1):
        print(max_area)         #-1結束後才印出最大
        print(max_line)
        break
    else:
        x_line = abs(n[0]-n[2])             #找出X
        y_line = abs(n[1]-n[3])             #找出Y
        Perimeter = 2*(x_line + y_line)     
        Area = x_line * y_line
        if(Perimeter>max_line):             #比大小
            max_line = Perimeter
        if(Area>max_area):
            max_area = Area