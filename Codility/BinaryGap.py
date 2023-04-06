ef solution(N):
    #convert the number into binary
    # L=[]
    k = bin(N)[2:]
    # str1=str(binary)
    # print(str1)
    countgap=0
    maxgap=0
    for i in k:
        if int(i)==0:
            countgap+=1
        elif int(i)==1:
            maxgap=max(maxgap,countgap)
            countgap=0
    # print(L)
    return maxgap
