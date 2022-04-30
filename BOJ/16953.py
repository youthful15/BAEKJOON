def find(x, y):
    global b, c
    
    if x > b or c != -1:
        return
    elif x == b:
        c = y
        return
    else:
        find(int(str(x) + '1'), y + 1)
        find(x * 2, y + 1)

a, b = map(int, input().split())
c = -1

find(a, 1)

print(c)