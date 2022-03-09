n, m = map(int, input().split())
lst = [input() for i in range(n)]
dna = ['T', 'G', 'C', 'A']
dict = {}
answer = ''
ans_num = 0

for i in range(m):
    
    max_num = 0
    max_a = ''
    
    for a in dna:
        dict[a] = 0
    
    for j in range(n):
        dict[lst[j][i]] += 1
        
    for key, value in dict.items():
        if value >= max_num:
            max_num = value
            max_a = key
            
    answer += max_a
    ans_num = ans_num + n - max_num
    
print(answer)
print(ans_num)