from re import T


def dfs(t):
    
    v1[t] = 1
    print(t, end = ' ')
    
    for i in lst[t]:
        if not v1[i]:
            dfs(i)
            
def bfs(t):
    
    if t == []:
        return
    
    new_lst = []
    
    for j in t:
        for i in lst[j]:
            if not v2[i]:
                print(i, end = ' ')
                v2[i] = 1
                new_lst.append(i)
            
    bfs(new_lst)


n, m, v = map(int, input().split())
lst = [[] for _ in range(n + 1)]
v1 = [0] * (n + 1)
v2 = [0] * (n + 1)
v2[v] = 1

for _ in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
    
for slst in lst:
    slst.sort()
    
dfs(v)
print()
print(v, end = ' ')
bfs([v])