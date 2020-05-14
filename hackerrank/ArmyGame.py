
def gameWithCells(n,m):
    area = (n + n%2) * (m + m%2)
    package = area / 4
    return int(package)
if __name__ == "__main__":
    n,m = list(map(int, input().split()))
    result = gameWithCells(n,m)
    print(result)