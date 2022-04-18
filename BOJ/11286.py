lst = []
lst2 = []

for _ in range(int(input())):
    
    a = int(input())
    
    if a > 0:
        lst.append(a)
        lst.sort()
    elif a < 0:
        lst2.append(a)
        lst2.sort(reverse=True)
    elif not lst and not lst2:
        print(0)
    elif not lst and lst2:
        print(lst2.pop(0))
    elif lst and not lst2:
        print(lst.pop(0))
    else:
        if lst[0] < -lst2[0]:
            print(lst.pop(0))
        else:
            print(lst2.pop(0))