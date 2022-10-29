def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True
def run_loop_till_prime(n,x):
    while is_prime(n) == False:
        n += x
    return n
t = int(input())
for i in range(t):
    n = int(input())
    pp = run_loop_till_prime(n, - 1)
    np = run_loop_till_prime(n, + 1)
    a = n - pp
    b = np - n
    if a < b:
        print(pp)
    elif a > b:
        print(np)
    else:
        print(min(pp,np))