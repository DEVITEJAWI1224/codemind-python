n = int(input())
a = str(n)
b = set(a)
if len(b) == len(a):
    print('Unique Number')
else:
    print('Not Unique Number')