case = int(input())
answer_lis = []

for three in range(case // 3 + 1):
    for five in range(case // 5 + 1):
        if three * 3 + five * 5 == case:
            answer_lis.append([three, five])
            
min_ans = 5000

for i in range(len(answer_lis)):
    if answer_lis[i][0] + answer_lis[i][1] < min_ans:
        min_ans = answer_lis[i][0] + answer_lis[i][1]

if min_ans == 5000:
    min_ans = -1
    
print(min_ans)