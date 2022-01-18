e,f,c = map(int,input().split())
s1 = (e + f) / c
final = s1
while s1 >= c :
    s1 = int(s1 / c)
    final += s1
print(int(final))