N, m, M, T, R = map(int, input().split())
now = m
exercise = 0
answer = 0
while exercise < N:
    if now + T <= M:
        now += T
        exercise += 1
    elif m + T > M:
        answer = -1
        break
    elif now - R >= m:
        now -= R
    else:
        now = m
    answer += 1

print(answer)