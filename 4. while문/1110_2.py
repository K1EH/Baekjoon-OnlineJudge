input=int(input())
N=input
count=0

while True:
    N=(N%10*10+(N//10+N%10)%10)
    count=count+1
    if N==input:
        break
    
print(count)