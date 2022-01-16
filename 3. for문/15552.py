import sys

count=int(input())
for x in range(count):
    a,b=map(int,sys.stdin.readline().strip().split())
    print(a+b)