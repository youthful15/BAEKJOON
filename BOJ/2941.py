alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

origin = input()
answer = len(origin)

for a in range(len(origin)):
    for b in alpha:
        if origin[a:a+len(b)] == b:
            answer -= len(b) - 1
            if  b == 'dz=':
                answer += 1
        
print(answer)