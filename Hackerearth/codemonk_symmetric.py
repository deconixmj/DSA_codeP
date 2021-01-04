t=int(input())
yn1=[]
for r in range(t):
    mat_size = int(input())
    x_mat_logo = [input() for i in range(mat_size)]

    y_mat = []

    for j in range(mat_size):
        str1 = ""
        for i in x_mat_logo:
            str1 += i[j]
        y_mat.append(str1)

    yn = []
    if mat_size % 2 !=0:

        total_compares=(mat_size-1)//2 +1


        if x_mat_logo[total_compares-1] == y_mat[total_compares-1]:
            yn.append("YES")
        else:
            yn.append("NO")

        for i in range(total_compares-1):
            if x_mat_logo[i]==x_mat_logo[-(i+1)]:
                yn.append("YES")
            else:
                yn.append("NO")

        for i in range(total_compares-1):
            if y_mat[i]==y_mat[-(i+1)]:
                yn.append("YES")
            else:
                yn.append("NO")

    else:
        total_compares=mat_size//2
        for i in range(total_compares):
            if x_mat_logo[i]==x_mat_logo[-(i+1)]:
                yn.append("YES")
            else:
                yn.append("NO")

        for i in range(total_compares):
            if y_mat[i]==y_mat[-(i+1)]:
                yn.append("YES")
            else:
                yn.append("NO")
    # print("\n")
    if "NO" in yn:
        yn1.append("NO")
    else:
        yn1.append("YES")


for i in yn1:
    print(i,end='\n')