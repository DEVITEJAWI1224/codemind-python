n = int(input())
n1 = 0
n2 = 1
s = n1 + n2
while (s < n):
    n1 = n2
    n2 = s
    s = n1+n2
if s == n:
    print('True')
else:
    print('False')