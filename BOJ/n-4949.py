while True :
    a = list(input())
    if a == ['.']:
        break
    
    so = 0
    dae = 0
    
    for word in a:
        if word == '(':
            so += 1
        if word == ')':
            so -= 1
        if word == '[':
            dae += 1
        if word == ']':
            dae -= 1
            
        if so < 0:
            print('no')
            break
        if dae < 0:
            print('no')
            break
        
        
        
    else:
        if so == 0 and dae == 0:
            print('yes')
        else:
            print('no')
        