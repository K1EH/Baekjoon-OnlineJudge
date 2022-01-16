A=int(input())
B=int(input())
C=int(input())

N=list(str(A*B*C))
index=[0 for i in range(10)]

for i in range(len(N)):
    for k in range(10):
        if int(N[i])==k:
            index[k]=index[k]+1
for i in range(10):
    print(index[i])