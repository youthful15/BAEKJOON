a = input()
b = input()
c = input()

if a == 'black':
    a = 0
elif a == 'brown':
    a = 10
elif a == 'red':
    a = 20
elif a == 'orange':
    a = 30
elif a == 'yellow':
    a = 40
elif a == 'green':
    a = 50
elif a == 'blue':
    a = 60
elif a == 'violet':
    a = 70
elif a == 'grey':
    a = 80
else:
    a = 90
    
if b == 'black':
    b = 0
elif b == 'brown':
    b = 1
elif b == 'red':
    b = 2
elif b == 'orange':
    b = 3
elif b == 'yellow':
    b = 4
elif b == 'green':
    b = 5
elif b == 'blue':
    b = 6
elif b == 'violet':
    b = 7
elif b == 'grey':
    b = 8
else:
    b = 9
    
if c == 'black':
    c = 1
elif c == 'brown':
    c = 10
elif c == 'red':
    c = 100
elif c == 'orange':
    c = 1000
elif c == 'yellow':
    c = 10000
elif c == 'green':
    c = 100000
elif c == 'blue':
    c = 1000000
elif c == 'violet':
    c = 10000000
elif c == 'grey':
    c = 100000000
else:
    c = 1000000000
    
print((a+b)*c)