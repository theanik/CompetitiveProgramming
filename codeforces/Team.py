n = int(input())
count = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    they = sum(arr)
    if they > 1:
        count += 1
print(count)