'''

find a position of letter in alphabet and add letters frm beginning to that position

'''
import string
S=input()
Upper=string.ascii_uppercase
Lower=string.ascii_lowercase
numbers="0123456789"
newS=""
for i in enumerate(S):
    if i[1].isupper():
        for j in enumerate(Upper):
            if j[1]==i[1]:
                newstr=Upper[:j[0]+1]
            else:
                continue

    elif i[1].islower():
        for j in enumerate(Lower):
            if j[1]==i[1]:
                newstr=Lower[:j[0]+1]
            else:
                continue

    elif i[1].isnumeric():
        for j in enumerate(numbers):
            if j[1]==i[1]:
                newstr=numbers[:j[0]+1]
            else:
                continue
    else:
        newstr=i[1]

    newS=newS+newstr
print(newS)
