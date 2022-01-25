while True :
    name = list(map(str,input().split()))
    if name[0] == '#' and name[1] == '0' and name[2] == '0' :
        break
    if name[1] > '17' or name[2] >= '80' :
        print('{0} Senior'.format(name[0]))
    else :
        print('{0} Junior'.format(name[0]))
