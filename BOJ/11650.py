case = int(input())
ans_lis = [0 for i in range(case)]

for i in range(case):
    ans_lis[i] = list(map(int, input().split()))
    
sorted_lis = sorted(ans_lis)

for i in range(case):
    print(sorted_lis[i][0],sorted_lis[i][1])