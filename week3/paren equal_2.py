def reconize(b):
    a = int(b[0])
    c = int(b[2])
    if(b[1]=='+'):
        return a+c
    elif(b[1]=='-'):
        return a-c
    elif(b[1]=='*'):
        return a*c
    elif(b[1]=='/'):
        return a/c
def main():
    recon = []
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
        print(Orgindata[maxflag+1:a])
        for i in range(maxflag+1,a):
            recon.append(Orgindata[i])
        cal = reconize(recon)
        print(cal)
    return 0
    
main()