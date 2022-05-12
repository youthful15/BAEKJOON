import sys
input = sys.stdin.readline

ans = list(input())
now = len(ans)

for _ in range(int(input())):
    k = input().rstrip()

    if k == 'L' and now >= 1:
        now -= 1
    elif k == 'D' and now < len(ans):
        now += 1
    elif k == 'B' and now > 0:
        now -= 1
        ans.pop(now)
    else:
        ans.insert(now, k[-1])
        now += 1

print(''.join(ans))
