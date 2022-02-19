for tc in range(int(input())):
    a, b = map(int, input().split())
    bae = yak = 0
    
    for i in range(max(a, b), 2 ** 99, max(a, b)):
        if i % min(a, b) == 0:
            bae = i
            break
        
    for i in range(min(a, b), 0, -1):
        if max(a, b) % i == 0 and min(a, b) % i == 0:
            yak = i
            break
        
    print(bae, yak)