import time
# Sieve of Eratosthenes

# n = int(input())
n= 1000000

def sieve(n):
    start_time = time.time()
    prime = [True for i in range(n + 1)] # boolen trure array
    # for i in range(4,n+1):
    #     if i % 2 == 0:
    #         prime[i] = False
    i = 2
    while i*i < n:
        if prime[i] == True:
            for j in range(i*2, n + 1,i):
                prime[j] = False
        i+=1
    prime[0] = False
    prime[1] = False
    # print(prime)
    count = 0
    for i in range(n + 1):
        if prime[i]:
            count += 1 
            print(i,end=" ")
    print("Total prime number : "+str(count))
    print("--- %s seconds ---" % (time.time() - start_time))

sieve(n)

# n = 10
# arr = []

# print(arr)

# arr = [True for i in range(11)]
# for i in range(11):
#     if i % 2 == 0:
#         arr[i] = False

# print(arr)