import heapq

import sys
input = sys.stdin.readline

lst = []

for _ in range(int(input())):
    a = int(input())

    if a:
        heapq.heappush(lst, a)
    else:
        try:
            print(heapq.heappop(lst))
        except:
            print(0)
