a,b=map(int,input().split())
s=list(map(int,input().split()))
for i in range(0,a,1) :
    if s[i]<b :
        print(s[i],end=' ')