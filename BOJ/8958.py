case = int(input())
for i in range(case):
    score = 0
    answer = list(input().split('X'))
    for o in answer:
        for i in range(len(o)):
            score += (i + 1)
    print(score)