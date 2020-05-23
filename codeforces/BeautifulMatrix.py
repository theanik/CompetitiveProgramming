matrix = []
for i in range(5):
    a,b,c,d,e = list(map(int, input().split()))
    matrix.extend([a,b,c,d,e])
getIndex = 0
for i in range(25):
    if matrix[i] == 1:
        getIndex = i

result = abs(getIndex - 12)
print(result)
# row = 0
# col = 0
# for i in range(5):
#     for j in range(5):
#         if matrix[i][j] == 1:
#             row = i
#             col = j
#             break
# result = abs(row - 2) + abs(col - 2)
# print(result)
# print(matrix)