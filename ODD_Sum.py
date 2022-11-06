n = int(input())
lst = list(map(int,input().split()))
#c = 0
s = 0
for i in lst :
    if i % 2 != 0 :
        s += i
print(s)