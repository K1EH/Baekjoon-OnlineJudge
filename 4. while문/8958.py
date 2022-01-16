case=int(input())

for i in range (case):
    ox=list(input())
    total=0
    point=1
    for k in range(len(ox)):
        if ox[k]=="O":
            total=total+point
            point=point+1
        else:
            point=1
    print(total)