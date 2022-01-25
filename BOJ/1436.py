case = int(input())
i = 0
number = 665
while i != case:
    number += 1
    if str(number).find('666') != -1:
        i += 1
print(number)