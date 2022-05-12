import itertools

a, b = map(int, input().split())
lst = [i for i in range(1, a + 1)]

answer = list(itertools.permutations(lst, b))

for ans in answer:
    print(*ans)
