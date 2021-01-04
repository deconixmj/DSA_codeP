t=int(input())
from collections import Counter
from itertools import chain

for _ in range(t):
    m,n=map(int,input().split())
    a=[]
    for i in range(m):
        a.append(input())

    s=input()
    sl=len(s)
    s2=""
    a2=[]
    s3=""
    s4=""
    temp = []

    while sl>0:
        for j in range(m):
            if sl>0:
                temp.append(j)
                sl -= 1

            else:
                break
    # print(temp)
    for i in range(len(s)):
       if s[i] in a[temp[i]]:
           s2+=s[i]
           a2.append((s[i],temp[i]))
           # break
       else:
           s4="NO"



    ot = Counter(chain(a2))
    # print(ot)

    if s4=="NO":
        print("No")
        break
    else:
        for i in range(len(a2)):
            if ot[a2[i]]<=3:
                s3="YES"
            else:
                s3="NO"
                break

        if s3=="YES":
            print("Yes")
        else:
            print("No")
