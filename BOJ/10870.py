def pib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    answer = pib(n - 1) + pib(n - 2)
    return answer

a = int(input())
print(pib(a))
    