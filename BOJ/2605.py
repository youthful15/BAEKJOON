a = int(input())
num = list(map(int,input().split()))
stu = list()
for i in range(a):
    stu.insert(i-num[i],i+1)
for i in range(a):
    print(stu[i],end=" ")