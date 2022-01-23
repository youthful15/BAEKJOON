case = int(input())
room_num = 1

if case == 1:
    print(case)
else:
    for i in range(1,1000000):
        room_num += i * 6
        if case <= room_num:
            print(i+1)
            break
    
