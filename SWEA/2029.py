case = int(input())
for i in range(case):
    a, b = map(int, input().split())
    print(f'#{i + 1} {a // b} {a % b}')