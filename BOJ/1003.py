lst = [[1, 0], [0, 1]]
inp = []

for _ in range(int(input())):
    inp.append(int(input()))
    
for s in range(max(inp) - 1):
        lst.append([lst[s][0] + lst[s + 1][0], lst[s][1] + lst[s + 1][1]])
   
for a in inp:        
    print(lst[a][0], lst[a][1])