a, b, c, d, e = map(int,input().split())
answer = (a * a + b * b + c * c + d * d + e * e) % 10
print(answer)