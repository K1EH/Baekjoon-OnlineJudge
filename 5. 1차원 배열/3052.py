import sys
numArr=[]
count=10

for i in range(10):
    numArr.append(int(sys.stdin.readline().strip())%42)
    for k in range(i-1,-1,-1):
        if numArr[i]==numArr[k]:
            count=count-1
            break
print(count)