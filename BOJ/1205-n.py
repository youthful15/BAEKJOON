n, new, p = map(int, input().split())
lst = list(map(int, input().split()))
lst.append(new)
lst.sort(reverse=True)

try:
    if n == p:
        for i in range(p):
            if lst[i] == new and lst[-1] != new:
                print(i + 1)
                break
        else:
            print(-1)
    else:
        for i in range(p):
            if lst[i] == new:
                print(i + 1)
                break
except:
    print(-1)
