member, kill = map(int, input().split())
lst = [i + 1 for i in range(member)]
print(lst)

print('<', end = '')
a = kill - 1 

for i in range(member):
    print(lst.pop(a))
    a -= i + 1
    if a + kill < len(lst):
        a += kill
    else:
        a = a + kill - len(lst)
    
print('>')