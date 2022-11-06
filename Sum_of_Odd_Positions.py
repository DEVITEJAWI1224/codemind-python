n = int(input())
lst = list(map(int,input().split()))
s = 0
for i in range(1,len(lst),2):
    s += lst[i]
print(s)