c = int(input())
lst_a = list(map(int, input().split()))
lst_b = list(map(int, input().split()))

lst_a.sort()
lst_b.sort(reverse=True)
answer = 0

for i in range(c):
    answer += (lst_a[i] * lst_b[i])
    
print(answer)
    