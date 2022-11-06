n = input()
lst = list(map(int,input().split()))
s = 0
for i in range(0,len(lst),2):
    s += lst[i]
print(s)