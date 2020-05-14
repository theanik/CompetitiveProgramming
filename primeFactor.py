def sieve(n):
    primeList = []

    prime = [True for i in range(n + 1)] # boolen trure array
    i = 2
    while i*i < n:
        if prime[i] == True:
            for j in range(i*2, n + 1,i):
                prime[j] = False
        i+=1
    prime[0] = False
    prime[1] = False
    count = 0
    for i in range(n + 1):
        if prime[i]:
            primeList.append(i)
    
    return primeList;


# def getPrimeFactor(n):
#     primeFactor = []
#     if n == 1:
#         return primeFactor
#     else:
#         primeOfthisNumber = sieve(n)
#         i = 0
#         while(primeOfthisNumber[i] < n):
#             if (n % primeOfthisNumber[i]) == 0:
#                 while(n%primeOfthisNumber[i] == 0):
#                     n = n / primeOfthisNumber[i]
#                     primeFactor.append(primeOfthisNumber[i]) 
#             i = i + 1
#     return primeFactor

# # print(getPrimeFactor(36))


# def uniqueFactor(list): 
  
#     unique_factor = [] 
      
#     for x in list: 
#         if x not in unique_factor: 
#             unique_factor.append(x)
#     return len(unique_factor)

# print(getPrimeFactor(500))
# print(uniqueFactor(getPrimeFactor(5000)))

def maxPrimefactorNum(N):  
  
    if (N < 2):  
        return 0;  
    
    prod = 1;
    count = 0;
    prime = sieve(N);
    for i in prime:
        prod = prod * i
        if prod <= N:
            count = count + 1

  
    return count;  
  
# Driver Code  
# N = 1;
# print(maxPrimefactorNum(N));  
