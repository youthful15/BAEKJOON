def plus(k):
    global n, ans
    
    if k < n:
        lst = [k + 1, k + 2, k + 3]
        for i in lst:
            plus(i)
    elif k > n:
        return
    else:
        ans += 1


for _ in range(int(input())):
    n = int(input())
    ans = 0
    plus(0)
    print(ans)