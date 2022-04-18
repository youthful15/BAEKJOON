for _ in range(int(input())):
    
    lst = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12]
    
    a = int(input())
    
    while len(lst) <= a:
        lst.append(lst[-1] + lst[-5])
        
    print(lst[a])