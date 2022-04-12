a = int(input())
lst = [a]
new_lst = []
temp = 0
ans = 0

while True:
    for num in set(lst):
        if num % 3 == 0:
            new_lst.append(num//3)
        if num % 2 == 0:
            new_lst.append(num//2)
        new_lst.append(num - 1)
        if num // 3 == 1 or num // 2 == 1 or num - 1 == 1:
            ans = 1
            break
    temp += 1
    lst = new_lst
    print(temp, lst)
    if ans:
        break
    
print(temp)