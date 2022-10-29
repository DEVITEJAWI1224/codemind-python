n = int(input())
lst = list(map(int,input().split()))
es = os = 0
for i in range(len(lst)):
    if i % 2 == 0:
        es += lst[i]
    else:
        os += lst[i]
print(abs(es - os))