N=int(input())

# N,L =int(input()),input().split()
# L=[input().split(' ') for i in range(N)]
#
# L.extend(input().split(' '))


L=[]
while len(L)!=N:
    L=input().split(' ')
    break

print(L)
print(any([i==i[::-1] for i in L]))

