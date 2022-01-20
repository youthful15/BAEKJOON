case = int(input())
scores = list(map(int, input().split()))
change_scores = [0 for i in range(case)]

for i in range(case):
    change_scores[i] = scores[i] / max(scores) * 100
    
print(sum(change_scores) / case)