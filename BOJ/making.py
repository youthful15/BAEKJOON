def find(i, j, time, trash):  # 현재 위치 i, j, 주운 시간, 쓰레기 개수

    global t, cnt, ans

    if t < time or ans < time:  # 시간 오버 했으면 ㅃ2
        return
    if trash == cnt:    # 쓰레기 다 주웠으면 값 넣기
        if time < ans:
            ans = time
            return

    dt = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    for (di, dj) in dt:
        ni = i + di
        nj = j + dj

        if 0 <= ni < 5 and 0 <= nj < 5 and v[ni][nj] == 0:
            v[ni][nj] = 1

            # 쓰레기 있을 경우 쓰레기 줍는 시간, 쓰레기 개수 더해서 다시 돌기
            if arr[ni][nj]:
                find(ni, nj, time + 1 + arr[ni][nj], trash + 1)
            else:                                                 # 쓰레기 없으면 그냥 다시 돌기
                find(ni, nj, time + 1, trash)

            v[ni][nj] = 0


t = int(input())
v = [[0] * 5 for _ in range(5)]

arr = [list(map(int, input())) for _ in range(5)]
cnt = 0

for i in range(5):      # 쓰레기 개수 세기
    for j in range(5):
        if 0 < arr[i][j] < 5:
            cnt += 1
        elif arr[i][j] == 5:    # 완택이 위치 찾기
            x = i
            y = j
            v[i][j] = 1

ans = 9999
find(x, y, 0, 0)        # 돌리기

if ans != 9999:          # answer 대입된 값 있으면 프린트, 없으면 -1
    print(ans)
else:
    print(-1)
