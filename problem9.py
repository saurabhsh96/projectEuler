#Constructing a pythagorian triplet
# m < n
import math

def triplet(m, n):
    a = n**2 - m**2
    b = 2*m*n
    c = n**2 + m**2
    return [a, b, c]

n = 2
li = []
while(1):
    for m in range(1, n):
        li = triplet(m, n)
        if(sum(li) == 1000):
            break
    if(sum(li) == 1000):
            break         
    n = n + 1

print(li)
print(math.prod(li))