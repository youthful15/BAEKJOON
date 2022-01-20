pass_word, try_word = map(int,input().split())
try_num = 1

for i in range(999):
    if pass_word == try_word:
        break
    else:
        try_word += 1
        try_num += 1
        
print(try_num)