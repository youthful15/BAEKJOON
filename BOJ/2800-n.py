import sys
from itertools import combinations
ids = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
ex = sys.stdin.readline().strip()
new = ''
answer = []

#괄호마다 id 부여(괄호 최대 10개)
ids = ids[:ex.count('(')]
idx = 0
for e in ex:
    if e=='(':
        new += ids[idx]
        idx += 1
    elif e==')':
        idx -= 1
        new += ids[idx]
    else:
        new += e

combis = []
for i in range(len(ids)):
    combis.extend(list(combinations(ids, i)))
    
for combi in combis:
    tmp = new
    for id in ids:
        if id in combi:
            tmp = tmp.replace(id, '(', 1)
            tmp = tmp.replace(id, ')', 1)
        else:
            tmp = tmp.replace(id, '', 1)
            tmp = tmp.replace(id, '', 1)
    answer.append(tmp)

answer = list(set(answer))
answer.sort()
print(*answer, sep = '\n')