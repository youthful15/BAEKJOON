import sys
case = int(sys.stdin.readline())

lst = []

for i in range(case):
    plz = sys.stdin.readline().strip()
    
    if plz[:4] == 'push':
        a, b = plz.split()
        lst.append(int(b))
        
    if plz == 'pop':
        try:
            print(lst.pop(-1))
        except:
            print('-1')
        
    if plz == 'size':
        print(len(lst))
        
    if plz == 'empty':
        if lst:
            print('0')
        else:
            print('1')
            
    if plz == 'top':
        if lst:
            print(lst[-1])
        else:
            print('-1')