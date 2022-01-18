N, m, M, T, R = map(int, input().split())
now = m
exercise = 0
answer = 0
while exercise < N:
    if now + T <= M:
        now += T
        exercise += 1
    elif now - R >= m:
        now -= R
    else:
        answer = -1
        break
    answer += 1

print(answer)