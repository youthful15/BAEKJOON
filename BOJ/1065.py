case = int(input())
answer = 99

lst = list(map(int, str(case)))

if case <= 99:
    print(case)
else:
    for i in range(100, case + 1):
        lst = list(map(int, str(i)))
        if lst[0] - lst[1] == lst[1] - lst[2]:
            answer += 1
    print(answer)