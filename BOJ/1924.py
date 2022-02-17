month, day = map(int, input().split())
answer = 0
lst = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

for i in range(month):
    answer += lst[i]
answer += day

day_lst = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
print(day_lst[answer % 7])