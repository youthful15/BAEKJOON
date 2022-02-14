a = int(input())
b = int(input())

lst = [True for i in range(b+1)]
lst[0] = lst[1] = False

for i in range(int(b ** 0.5) + 1):
    if lst[i]:
        try:
            for j in range(2,10000):
                lst[i*j] = False
        except:
            pass
        
answer = 0
min = b

for i in range(b, a-1, -1):
    if lst[i]:
        answer += i
        min = i

if answer == 0:
    print(-1)
else:
    print(answer)
    print(min)