## final submit

'''
You will be told & displayed N numbers in a line ,
Questioner will ask you M questions
For each question he will show you a number and you need to tell if that number is present in above list of numbers --
if yes how may times and if not , print "not present"

'''

n=int(input())
display_nos = list(map(int, input().split()))
no_query=int(input())
L=[]
questioner=[]
output=[]
for i in range(no_query):
    L.extend([x for x in input()])  # why extend and no append here.
questioner=[int(x) for x in L]
for k in questioner:
    if k not in display_nos:
        output.append("NOT PRESENT")
    else:
        no_occurrances = 0
        for i in display_nos:
            if i==k:
                no_occurrances += 1
        output.append(no_occurrances)
for m in output:
    print (m)
