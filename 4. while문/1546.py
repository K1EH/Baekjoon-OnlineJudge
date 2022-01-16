N=int(input())
grade=list(map(int,input().split()))
total=0
max=max(grade)

for i in range (N):
    grade[i]=grade[i]/max*100
    total=total+grade[i]
    
print(total/N)