m, n, h = map(int, input().split())

dx = [[0, 1, 0], [0, 0, 1], [0, -1, 0], [0, 0, -1], [1, 0, 0], [-1, 0, 0]]
arr = []
lst = []
ans = 0


for _ in range(h):
    arr += [[list(map(int, input().split())) for i in range(n)]]

for f in range(h):
    for s in range(n):
        for t in range(m):
            if arr[f][s][t] == 1:
                lst.append([f, s, t])
                
while lst:
    new_lst = []
    
    while lst:
        f, s, t = lst.pop()
        for df, ds, dt in dx:
            nf, ns, nt = f + df, s + ds, t + dt
            if 0 <= nf < h and 0 <= ns < n and 0 <= nt < m and arr[nf][ns][nt] == 0:
                arr[nf][ns][nt] = 1
                new_lst.append([nf, ns, nt])
                
    ans += 1
    lst = new_lst

for f in range(h):
    for s in range(n):
        for t in range(m):
            if arr[f][s][t] == 0:
                ans = 0

print(ans - 1)