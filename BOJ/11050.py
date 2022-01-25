a, b = map(int,input().split())

bunja = a
bunmo = b

if b == 0:
    print('1')
else:
    for i in range(1,a):
        bunja *= i
        
    for i in range(1,b):
        bunmo *= i
        
    for i in range(1,a-b+1):
        bunmo *= i
        
    print(int(bunja / bunmo))