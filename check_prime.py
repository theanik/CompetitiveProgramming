
# def isPrime(n):
#     if n <= 1:
#         return False
#     i = 2
#     while i*i < n:
#         if n % i == 0:
#             return False
#         i = i + 1
#     return True

# n = 120
# primes = []
# for i in range(120):
#     if isPrime(i):
#         primes.append(i)

# print(primes)

# def printPime(n):
#     if n <= 1:
#         return False
#     i = 2
#     while i*i < n:
#         if n % i == 0:
#             continue
#     print(i)
#     i+=1
# printPime(100)


for i in range(2,30):
    flag = 1
    for j in range(2,i):
        if i % j == 0:
            flag = 0
            break
    if flag == 1:
        print(i,end=" ")


# print(10//2)

