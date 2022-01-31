case = int(input())

sum = 0
for i in range(1, case + 2):
    sum += i
    if sum > case:
        break

print(i - 1)