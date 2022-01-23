case = int(input())
num_std = 0

for i in range(case):
    sum_score, num_std = 0, 0
    score_list = list(map(int, input().split()))
    for j in range(score_list[0]):
        sum_score += score_list[j+1]
    ave_score = sum_score / score_list[0]
    for j in range(score_list[0]):
        if score_list[j+1] > ave_score:
            num_std += 1
    print('%.3f%%' %round(num_std / score_list[0] * 100, 3))