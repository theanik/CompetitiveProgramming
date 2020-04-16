print("Enter the number of element")
noe = int(input())
data = []
for _ in range(noe):
    data.append(input())

print("Enter ",noe," sorted number")

for i in range(len(data)):
    print(data[i])

print("Enter search value")
sv = input()

lb = 0
up = noe - 1
mid = (lb+up) / 2
mid = round(mid)

while lb <= up:
    if data[mid] < sv:
        lb = mid + 1
    elif data[mid] == sv:
        print(sv+" is present on location",mid+1)
        break
    else:
        up = mid -1
if lb > up:
    print(sv,"is not present in this list")
