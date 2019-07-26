a=int(input())
b=list(map(int,input().split()))
l=[]
for i in range(len(b)):
    if(i==b[i]):
        l.append(b[i])
print(*l)
