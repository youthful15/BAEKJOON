num = int(input())
for i in range(num):
    q = str(input())
    if list(q)[0] == 'P':
        print('skipped')
    else :
        q2 = list(q.split('+'))
        print(int(q2[0]) + int(q2[1]))