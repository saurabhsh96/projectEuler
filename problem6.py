import math as m
n = 100
sum_square = m.pow(n * (n + 1) / 2, 2)
square_sum = n * (n + 1) * (2*n + 1) / 6
diff = abs(sum_square - square_sum)
print(diff)