mo = ['a', 'e', 'i', 'o', 'u']
a = input()

while a != '#':
    answer = 0
    for i in a:
        if i.lower() in mo:
            answer += 1
    print(answer)
    a = input()