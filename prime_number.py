import math as m
def prime_num(n):
    if n == 1:
        return False
    sq = int(m.sqrt(n))
    for i in range(2,sq + 1):
        if n % i == 0:
            return False
    return True
n = int(input())
if prime_num(n):
    print('prime')
else:
    print('not a prime')