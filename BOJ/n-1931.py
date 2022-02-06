a = int(input())
lst = [0 for i in range(a)]

for i in range(a):
    lst[i] = list(map(int,input().split()))
    
lst.sort()
cnt = 0
answer = 0

for i in range(a):
    