def fibonacci(s):
    global z, o
    
    if s == 0:
        z += 1
        return
    elif s == 1:
        o += 1
        return
    else:
        fibonacci(s - 1)
        fibonacci(s - 2)
        

for _ in range(int(input())):
    z = o = 0
    a = int(input())
    fibonacci(a)
    
    print(z, o)