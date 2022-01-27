import sys

case = int(sys.stdin.readline())
deque = []

for i in range(case):
    plz = sys.stdin.readline().strip()
    
    if plz[:10] == 'push_front':
        plz, a = plz.split()
        deque.insert(0, int(a))
        
    if plz[:9] == 'push_back':
        plz, a = plz.split()
        deque.append(int(a))
        
    if plz == 'pop_front':
        if len(deque) == 0:
            print('-1')
        else:
            print(deque.pop(0))
        
    if plz == 'pop_back':
        if len(deque) == 0:
            print('-1')
        else:
            print(deque.pop())
        
    if plz == 'size':
        print(len(deque))
        
    if plz == 'empty':
        if len(deque) == 0:
            print('1')
        else:
            print('0')
            
    if plz == 'front':
        if len(deque) == 0:
            print('-1')
        else:
            print(deque[0])
            
    if plz == 'back':
        if len(deque) == 0:
            print('-1')
        else:
            print(deque[-1])