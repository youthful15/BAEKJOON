a = int(input())
lst = list(map(int, input().split()))
answer = min(lst) * max(lst)
print(answer)