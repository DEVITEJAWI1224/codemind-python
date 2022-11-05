n=int(input())
n1=0
n2=1
s=n1+n2
while(s<=n):
    n1=n2
    n2=s
    s=n1+n2
if abs((s-n)> abs(n2-n)):
    print(n2)
elif (abs(s-n)==abs(n2-n)):
    a=(n2,s)
    print(*a)
    
else:
    ans=s
    print(ans)