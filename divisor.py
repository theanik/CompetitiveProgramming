# get how many divisor in a number

'''
এটার টাইম কম্প্লেক্সিটি O(n)
'''
n = 18

def getDivisor(n):
    count = 0
    for i in range(1,n+1):
        # if i == n:
        #     continue
        if n % i == 0:
            count += 1
            print(i)
    print("total divisor "+str(count))

getDivisor(n)


'''
এটার টাইম কম্প্লেক্সিটি O(root(n))
'''
n = 999999
def getDivisorRootN(n):
    count = 0
    i = 1
    while i * i < n+1:
        if n == i*i:
            print(i)
            count += 1
        elif n % i == 0:
            print(i)
            print(int(n/i))
            count +=2
        i += 1
    print("total count of divisor "+str(count))

getDivisorRootN(n)
print(16%1 == 0)


