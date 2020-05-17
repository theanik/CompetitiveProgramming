import math

def summingSeries(n):
    if n == 1:
        return 1
    summing = 0
    for i in range(1,n+1):
        summing += math.pow(i,2) - math.pow((i - 1),2)
    return int(summing)


t = int(input())

for t_itr in range(t):
    n = int(input())

    result = summingSeries(n)
    print(result)



