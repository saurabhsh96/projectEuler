count = 1
num = 2
primes = []

def isPrime(num):
    flag = 1
    for i in range(2, int(num/2) + 1):
        if(num%i == 0):
            flag = 0
            break
    return flag

while(count != 10002):
    isP = 0
    isP = isPrime(num)
    if(isP == 1):
        primes.append(num)
        count = count + 1
        #print(count, num)
    num = num + 1

print(primes[10000])