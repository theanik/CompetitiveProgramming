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


def maxPrimefactorNumProductGatterthenN(n):
    if (n < 2):  
        return 0;      
    prod = 1;
    count = 0;
    prime = sieve(n); #[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for i in prime:
        prod = prod * i
        if prod <= n:
            count = count + 1
    return count;


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        result = maxPrimefactorNumProductGatterthenN(n)
        print(result)