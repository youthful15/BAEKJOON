case = int(input())
num_list = list(map(int, input().split()))
sosu = 0

for num in num_list:
    mang = 0
    for i in range(2, num - 1):
        if num % i == 0:
            mang = 1
            break
    if mang == 1:
        continue
    sosu += 1 
    
if 1 in num_list:
    sosu -= 1
            
print(sosu)