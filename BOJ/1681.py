n, l = map(int, input().split())

ans = 1
person = 0

while person != n:
    if str(l) in str(ans):
        pass
    else:
        person += 1
    ans += 1
    
print(ans - 1)