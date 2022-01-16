N=[0 for i in range(9)]
max=int(0)
seq=0

for i in range(9):
    N[i]=int(input())
    if max<N[i]:
        max=N[i]
        seq=i
print("%d\n%d" %(max,seq+1))