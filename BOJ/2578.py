import sys
input = sys.stdin.readline

cheol = {0 : [], 1 : [], 2 : [], 3: [], 4 : []}
call = []

for i in range(5):
    cheol[i] += list(map(int, input().split()))
                     
for i in range(5):
    call += list(map(int, input().split()))
    
cnt = 0

for num in call:
    bingo = 0
    cnt += 1
    
    for i in range(len(cheol)):
        if num in cheol[i]:
            dex = cheol[i].index(num)
            cheol[i].pop(dex)
            cheol[i].insert(dex, 'x')
            break
    
    for i in range(5): #가로줄
        for j in range(5):
            if cheol[i][j] != 'x':
                break
        else:
            bingo += 1
    
    for j in range(5): #세로줄
        for i in range(5):
            if cheol[i][j] != 'x':
                break
        else:
            bingo += 1
            
    for i in range(5): #왼쪽 대각선
        if cheol[i][i] != 'x':
            break
    else:
        bingo += 1
            
    for i in range(4, -1, -1): #오른쪽 대각선
        if cheol[abs(i-4)][i] != 'x':
            break
    else:
        bingo += 1
        
    if bingo >= 3:
        break
    
    
print(cnt)