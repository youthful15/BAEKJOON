a = list(input().upper())
lst_a = list(set(a))
ans_a = [0 for i in range(len(lst_a))]

for alpha_a in a:
    for i in range(len(lst_a)):
        if alpha_a == lst_a[i]:
            ans_a[i] += 1
            
max_cnt = 0

for i in ans_a:
    if i == max(ans_a):
        max_cnt += 1
        
if max_cnt > 1:
    print('?')
else:
    print(lst_a[ans_a.index(max(ans_a))])