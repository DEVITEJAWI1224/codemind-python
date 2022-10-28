n = int(input())
t = abs(n)
s = 0
while t > 0:
    r = t % 10
    s = s * 10 + r
    t = t // 10
if n < 0:
    print(-s)
else:
    print(s)