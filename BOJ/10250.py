for tc in range(int(input())):
    h, w, n = map(int, input().split())
    
    b = (n - 1) // h + 1
    a = n - ((b - 1) * h)
    
    if b >= 10:
        print(f'{a}{b}')
    else:
        print(f'{a}0{b}')