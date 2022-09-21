n = int(input())
p = 1
s = 0
while n > 0:
    r = n % 10
    p *= r
    s += r
    n = int(n / 10)
    z = p - s
print(z)