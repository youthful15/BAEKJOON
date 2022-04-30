for tc in range(int(input())):
    dict = {}
    
    for _ in range(int(input())):
        a, b = input().split()
        
        if b in dict:
            dict[b] += 1
        else:
            dict[b] = 2
            
    ans = 1
    
    for a in dict.values():
        ans *= a
        
    print(ans - 1)