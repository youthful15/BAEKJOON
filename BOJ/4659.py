a = input()
mo = ['a', 'i', 'e', 'o', 'u']
check = 0
ac = 'acceptable'
noac = 'not acceptable'

while a != 'end':
    for i in range(len(a)):
        if a[i] in mo:
            check = 1
            break
        
    for i in range(len(a) - 1):
        try:
            if a[i] == a[i + 1] and a[i] != 'e' and a[i] != 'o':
                check = 0
                break
        except:
            pass
        
    for i in range(len(a) - 2):
        try:
            if a[i] in mo and a[i + 1] in mo and a[i + 2] in mo:
                check = 0
                break
            elif a[i] not in mo and a[i + 1] not in mo and a[i + 2] not in mo:
                check = 0
                break
        except:
            pass
        
    print(f'<{a}> is {ac if check else noac}.')
    a = input()
    check = 0