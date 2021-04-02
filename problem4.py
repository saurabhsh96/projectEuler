def isPalin(a):
    #counter = 0
    flag = 1
    digits = []
    temp = a
    while(temp>0):
        rem = temp%10
        digits.append(rem)
        temp = int(temp/10)
    for i in range(int(len(digits)/2)):
        if(digits[i] != digits[len(digits)-1-i]):
            flag = 0
            break
    #print(flag)
    return flag

palindrome = []
for i in range(900, 999):
    for j in range(900, 999):
        a = i*j
        res = isPalin(a)
        if(res == 1):
            palindrome.append(a)
            print(i, j)
print(max(palindrome))