# from string import ascii_letters

import string
n=int(input())
L=[]
L1=[]

for i in range(n):
    name=input()
    grades=float(input())
    print([name,grades])
    L.append([name,grades])

# L1=[]
for i in L:
    L1.append(i[1])


L2=sorted(list(set(L1)))
# L2.sort()
# for j in L1:
#     if j in L:

print(L2)
# print(L)
L3=[]
for j in L:
    if L2[1]==j[1]:
        L3.append(j[0])

print(L3)
L4=[]
for k in L3:
    # print(k[0][0])
    a=string.ascii_uppercase.index(k[0][0])
    L4.append(a)

L4.sort()
print(L4)

if len(set(L4)) ==1:
    for i in L3:
        print(i)
else:
    for i in L4:
        b=string.ascii_uppercase[i]

        for j in L3:
            if b in j:
                print(j)




