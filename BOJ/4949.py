a = input()
gwalho = ['[', '(', ')', ']']

while a != '.':
    lst = [0 for _ in range(100)]
    top = 0
    for i in a:
        try:
            if i == '[' or i == '(':
                lst[top] = i
                top += 1
            elif i == ']':
                if lst[top - 1] == '[':
                    top -= 1
                else:
                    print('no')
                    break
            elif i == ')':
                if lst[top - 1] == '(':
                    top -= 1
                else:
                    print('no')
                    break
        except:
            print('no')
            break
    else:
        if top == 0:
            print('yes')
        else:
            print('no')
    a = input()
            
    