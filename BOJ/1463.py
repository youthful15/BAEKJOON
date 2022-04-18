a = int(input())
lst = [a]
new_lst = []
v = [0] * (10 ** 6 + 1)
v[a] = 1 
temp = 0

while v[1] == 0:
    new_lst = []
    
    for num in lst:
        v[num] = 1
        if num % 3 == 0 and v[num // 3] == 0:
            v[num // 3] = 1
            new_lst.append(num // 3)
        if num % 2 == 0 and v[num // 2] == 0:
            v[num // 2] = 1
            new_lst.append(num // 2)
        if v[num - 1] == 0:
            v[num - 1] = 1
            new_lst.append(num - 1) 
            
    temp += 1
    lst = new_lst
    
print(temp)