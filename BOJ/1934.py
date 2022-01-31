import sys
import math
input = sys.stdin.readline

case = int(input())

for i in range(case):
    a, b = map(int, input().split())
    print(math.lcm(a, b))
    
    # for c in range(max(a, b), a * b + 1, max(a, b)):
    #     if c % min(a, b) == 0:
    #         print(c)
    #         break