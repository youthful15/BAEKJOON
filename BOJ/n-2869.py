day, night, long = map(int, input().split())
answer = 0
length = 0

while True:
    answer += 1
    length += day
    if length >= long:
        print(answer)
        break
    length -= night