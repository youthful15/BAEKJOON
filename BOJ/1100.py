lst = [input() for i in range(8)]
answer = 0

for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0:
            if lst[i][j] == 'F':
                answer += 1
        if i % 2 == 1 and j % 2 == 1:
            if lst[i][j] == 'F':
                answer += 1
                
print(answer)

