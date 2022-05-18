lst = [0] * 26

while True:
    try:
        words = input()
        if words == '':
            break
        for i in words:
            if i != ' ':
                lst[ord(i.upper()) - 65] += 1
    except:
        break

if max(lst) != 0:
    for i in range(26):
        if lst[i] == max(lst):
            print(chr(97 + i), end='')
