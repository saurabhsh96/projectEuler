import math as m

def isPrime(n):
    if(n == 1):
        return False
    elif(n < 4):
        return True
    elif(n % 2 ==0):
        return False
    elif(n < 9):
        return True
    elif(n % 3 ==0):
        return False
    else:
        limit = int(m.sqrt(n))
        f = 5 #Number that will decide primes
        while( f<= limit):
            if(n%f == 0):
                return False
            elif(n%(f+2) == 0):
                return False
            f = f + 6
        return True

limit = 100001
count = 1
current_number = 1
while(count!=limit):
    current_number = current_number + 2
    if(isPrime(current_number)):
        count = count + 1

print(current_number)