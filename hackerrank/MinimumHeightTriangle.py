import math

def triangleHight(base,area):
    hight = (2 * area) / base
    return math.ceil(hight)

if __name__ == "__main__":
    base,area = input().strip().split(' ')
    base,area = [int(base),int(area)]
    result = triangleHight(base,area)
    print(result)