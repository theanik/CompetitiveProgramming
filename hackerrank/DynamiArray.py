n,q = list(map(int, input().split()))

sqList = []

for i in range(n):
    sqList.append([])
lastAns = 0

for j in range(q):
    numbers= list(map(int, input().split()))
    x,y = numbers[1],numbers[2]
    if numbers[0] == 1:
        seq = (x ^ lastAns) % n
        sqList[seq].append(y)
    else:
        seq = (x ^ lastAns) % n
        index = y % len(sqList[seq])
        lastAns = sqList[seq][index]
        print(lastAns)