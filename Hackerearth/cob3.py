T1=input()
for i in range(int(T1)): # for each testcase , input green and purple baloon price
    gb_count,pb_count= 0,0
    x,y=list(map(int,input().split())) # enter price of green and purple baloon
    Participants = input() # enter no of participant
    for j in range(int(Participants)): # for each participant input problem solved or NOT
        m,n=list(map(int,input().split()))
        if m:
            gb_count += 1
        if n:
            pb_count += 1
    if i%2==0:
        TP=x*gb_count + y*pb_count
        print("{}".format(TP))
    else:
        TP=y*gb_count + x*pb_count
        print("{}".format(TP))
