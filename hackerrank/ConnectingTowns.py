def connectingTowns(routes):
    pathsum = 1
    for i in routes:
        pathsum = (pathsum * i) % 1234567
    return pathsum



t = int(input())

for _ in range(t):
    n = int(input())

    routes = list(map(int, input().split()))

    result = connectingTowns(routes)
    print(result)