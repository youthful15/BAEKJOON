for _ in range(int(input())):
    n, m = map(int, input().split())
    
    if n < m:
        n, m = m, n
        
    ans = 1
    
    if n == m:
        pass
    else:
        for i in range(n, n - m, -1):
            ans *= i
            ans /= (n - i + 1)
        
    print(int(ans))