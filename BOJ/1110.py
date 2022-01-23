case = input()
bef_num = case
aft_num = -1
answer = 0

while int(aft_num) != int(case):
    if int(bef_num) < 10:
        if list(bef_num)[0] == '0': #'07'같은 게 들어있을 시 잘라냄...
            bef_num = list(bef_num)[-1]
        sum_num = bef_num
        aft_num = bef_num + bef_num
    else:
        sum_num = int(list(bef_num)[0]) + int(list(bef_num)[1])
        aft_num = list(bef_num)[1] + list(str(sum_num))[-1]
    answer += 1
    bef_num = aft_num
print(answer)