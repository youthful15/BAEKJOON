s = input()
lst = []
for i in range(len(s) + 1):
    lst += [s[i:len(s)]]

lst.sort()

for i in range(1, len(s) + 1):
    print(lst[i])