n=int(input())
m=list(map(int,input().split()))
stack=[[]]
lot=[]

for i in range(len(m)+1):
    for j in range(i+1,len(m)+1):
        sub=m[i:j]
        stack.append(sub)

        if len(sub) >1:

            j=max(sub)
            j1=sub.index(j)+1
            k2=sorted(sub)[-2]
            ki2=sub.index(k2)+1
            if ki2 < j1:
                lot.append((ki2,j1))

print(len(set(lot)))




