import sys
a=int(input())
for i in range(1,a+1,1) :
    a,b=map(int,sys.stdin.readline().split())
    print(a+b)