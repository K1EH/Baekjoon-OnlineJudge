N=int(input())
num=list(map(int,input().split()))
max=num[0]
min=num[0]

for i in range(N):
    if max<num[i]:
        max=num[i]
    if min>num[i]:
        min=num[i]

print(min,max)