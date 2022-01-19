import time
t1 = time.time()

word = input().upper()
answer_dict = {}

for word_alpha in list(word):
    try:
        answer_dict[word_alpha] += 1
    except:
        answer_dict[word_alpha] = 1

print(answer_dict)

t2 = time.time()
print(t2-t1)