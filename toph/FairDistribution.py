x,y = map(int, input().split())
c = y
while(y%x!=0):
    y += 1
print(y - c)