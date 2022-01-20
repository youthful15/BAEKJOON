sound = list(map(int, input().split()))
ascending = 0
descending = 0

for i in range(len(sound) - 1):
    if sound[i] + 1 == sound[i + 1]:
        ascending += 1
    if sound[i] - 1 == sound[i + 1]:
        descending += 1

if ascending == 7:
    print("ascending")
elif descending == 7:
    print("descending")
else:
    print("mixed")