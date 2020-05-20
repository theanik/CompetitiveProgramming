n,m,a= map(int, input().strip().split())

if n % a == 0:
    l = n//a
else:
    l = (n//a)+1
if m % a == 0:
    w = m // a
else:
    w = (m//a)+1

print(l*w)