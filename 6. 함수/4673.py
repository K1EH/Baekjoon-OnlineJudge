#str로 처리
def d (n: int):
    n_=str(n)
    temp=0
    for i in range(len(n_)):
        temp+=int(n_[i])
    return(n+temp)
noSelfNum=[]
for i in range(10001):
    noSelfNum.append(d(i))
    if i not in noSelfNum:
        print(i)
        
#int로 처리
def d (n:int):
    n_=str(n)
    sum=n
    for i in range(len(n_)):
        rest=n%10
        sum+=rest
        n=n//10
    return sum

numbers=set()
nonSelfNum=set()
for i in range(10000):
    numbers.add(i)
    nonSelfNum.add(d(i))

selfNum=numbers-nonSelfNum
for i in sorted(selfNum):
    print(i)
