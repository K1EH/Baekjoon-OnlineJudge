N,X=map(int,input().split())

list=list(input().split())

for i in range(N):
    if (int(list[i])<X):
        print(list[i],end=" ")