i = 1

while True:
    
    a = int(input())
    if a == 0:
        break
    
    lst = [0]
    ans = [0] * (a + 1)
    ans[0] = 2
    
    for _ in range(a):
        lst.append(input())
        
    for _ in range(2 * a - 1):
        b, c = input().split()
        ans[int(b)] += 1
        
    print(i, lst[ans.index(1)])
    i += 1