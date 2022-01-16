def aSeq(n:int):
    return n//100+n%10==2*((n//10)%10)

def hansoo(n: int):
    count=0
    for i in range(1,n+1,1):
        if i<100:
            count+=1
        else:
            if aSeq(i):
                count+=1
    print(count)
    
hansoo(int(input()))