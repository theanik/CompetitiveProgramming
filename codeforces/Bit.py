t = int(input())
n = 0
for _ in range(t):
    s = input()
    if s == '++X' or s == 'X++':
        n += 1
    if s == '--X' or s == 'X--':
        n -= 1
print(n)