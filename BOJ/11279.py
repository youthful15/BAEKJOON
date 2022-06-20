import heapq
import sys
input = sys.stdin.readline

lst = []

for _ in range(int(input())):
    a = int(input()) * -1

    if a:
        heapq.heappush(lst, a)
    else:
        try:
            print(heapq.heappop(lst) * -1)
        except:
            print(0)
