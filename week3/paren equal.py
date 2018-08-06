def main():
    parenflag = 0
    maxflag = 0
    strparen = ")"
    Orgindata = input()
    a = Orgindata.find(strparen)
    for i in range(len(Orgindata)):
        if(Orgindata[i]=='('):
            parenflag += 1
            maxflag = i
        if(Orgindata[i]==')'):
            parenflag -= 1

    if(parenflag!=0):
        print("ERROR INPUT")
    else:
        b = Orgindata[maxflag+1:a]
        print(b)
        print(eval(b))
    return 0
    
main()