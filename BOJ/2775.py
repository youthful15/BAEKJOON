for tc in range(int(input())):
    k = int(input())
    n = int(input())
    lst = [i for i in range(1, n + 1)]
    
    for i in range(1, k + 1):
        new_lst = [1]
        for j in range(1, n):
            new_lst += [new_lst[j - 1] + lst[j]]
        lst = new_lst
        
    print(lst[n - 1])
            