import math as m
number = 600851475143
prime_factors = []

def factor(number):
    isP = 0
    for i in range(2, int(number/2)):
        if(number%i == 0):
            isP = isPrime(i)
        if(isP == 1):
            prime_factors.append(i)
            break
    next_num = number/i
    isP = isPrime(next_num)
    if(isP == 1):
        prime_factors.append(next_num)
    else:
        factor(next_num)    
            
def isPrime(num):
    flag = 1
    for i in range(2, int(num/2)):
        if(num%i == 0):
            flag = 0
            break
    return flag

factor(number)
print(prime_factors)