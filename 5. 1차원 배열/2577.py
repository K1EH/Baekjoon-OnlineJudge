A=int(input())
B=int(input())
C=int(input())

mux=str(A*B*C)
for i in range(10):
    cnt=0
    for k in range(len(mux)):
        if mux[k]==str(i):
            cnt=cnt+1
    print(cnt)