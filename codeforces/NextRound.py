n,k = map(int, input().strip().split())
score = list(map(int, input().split()))
count = 0
for i in range(n):
    if score[i] >= score[k-1] and score[i] > 0:
        count += 1
print(count)