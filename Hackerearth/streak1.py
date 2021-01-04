import re
num=int(input())
#reg=re.compile(["2*1"])
for i in range(num):
    num1=int(input())
    if (num1 % 21 == 0 ) or (("21" in str(num1)) or ("2*1" in str(num1))):
        print("The streak is broken")
    else:
        print("The streak lives still in our heart!")
