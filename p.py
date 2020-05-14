import time

start_time = time.time()
sum = 0
for i in range(1,100000):
    sum += i
print(sum)


print("--- %s seconds ---" % (time.time() - start_time))