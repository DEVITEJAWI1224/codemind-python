n = int(input())
n1 = 0
n2 = 1
s = 0
for i in range(0,n):
    print(s, end = ' ')
    n1 = n2
    n2 = s
    s = n1 + n2
    