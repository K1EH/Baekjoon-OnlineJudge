import sys
case=int(input())

for i in range(case):
    total=0
    p=0
    grade=list(map(int,sys.stdin.readline().strip().split()))
    for k in range (grade[0]):
        total=total+grade[k+1]
    avg=total/grade[0]
    for k in range (grade[0]):
        if grade[k+1]>avg:
            p=p+1
    print("%5.3f" %(p/grade[0]*100)+"%")