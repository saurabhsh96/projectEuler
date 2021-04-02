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

current_number = 1
sum = 0
while(current_number<=2000000):
    if(isPrime(current_number)):
        sum = sum + current_number
        #print( current_number)
    if(current_number < 3):
        current_number = current_number + 1
    else:
        current_number = current_number + 2

print(sum)