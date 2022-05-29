n = int(input())
lst = list(map(int, input().split()))
M = Y = 0

for t in lst:
    Y += (t // 30 + 1) * 10
    M += (t // 60 + 1) * 15

if M < Y:
    print('M', M)
elif M == Y:
    print('Y', 'M', Y)
else:
    print('Y', Y)
