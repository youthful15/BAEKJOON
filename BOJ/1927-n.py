import sys
input = sys.stdin.readline
lst = []
q = 0

for _ in range(int(input())):
    a = int(input())
    
    if a:
        lst.append(a)
    else:
        if lst:
            print(min(lst))
            lst.remove(min(lst))
            
        else:
            print(0)