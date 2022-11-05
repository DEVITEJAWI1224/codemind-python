n = int(input())
sq = 0
s = 0
while n > 0:
    r = n % 10
    sq += r ** 2
    s += sq
    n = n // 10
    if n == 0 and sq > 9:
        n = sq
        sq = 0
if sq == 1:
    print('True')
else:
    print('False')