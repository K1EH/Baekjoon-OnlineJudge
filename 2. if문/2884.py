h,m=map(int,input().split())

if (h==0 and m<45):
    h=23
    m=m+15
elif(m<45):
    h=h-1
    m=m+15
else:
    m=m-45

print(h,m)