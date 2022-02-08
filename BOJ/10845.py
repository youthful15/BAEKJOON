from collections import deque
import sys
input = sys.stdin.readline

deq = deque()
case = int(input())
for i in range(case):
    a = input().rstrip()
    
    if a[:3] == 'pus':
        a, b = a.split()
        deq.append(int(b))
    elif a == 'size':
        print(len(list(deq)))
    elif a == 'pop':
        if list(deq):
            print(deq.popleft())
        else:
            print(-1)
    elif a == 'empty':
        if list(deq):
            print(0)
        else:
            print(1)
    elif a == 'back':
        if list(deq):
            print(list(deq)[-1])
        else:
            print(-1)
    elif a == 'front':
        if list(deq):
            print(list(deq)[0])
        else:
            print(-1)