def solve(a: list):
    sum=0
    for i in range(len(a)):
        sum=sum+a[i]
    return sum

print(solve([1,2,4]))
