N=input().zfill(2)
nN=N
count=0

try:
    while True:
        sum=(int(nN[0])+int(nN[1]))
        sum=str(sum).zfill(2)
    
        nN=(nN[1]+sum[1])
        count+=1
        if nN==N:
            print(count)
            break;
except:
    print("error")




    