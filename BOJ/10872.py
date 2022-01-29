def fac(num):
    if num > 1:
        answer = num * fac(num - 1)
    else:
        return 1
    return answer

a = int(input())
print(fac(a))