lst = [0] * 26
# 소문자 a 97, 대문자 A 65

for tc in range(int(input())):
    words = input()
    word_lst = words.split()

    for word in word_lst:
        if not lst[ord(word[0].upper()) - 65]:
            lst[ord(word[0].upper()) - 65] = 1
            if len(word_lst) == 1:
                print(f'[{word[0]}]{word[1:]}')
            else:
                for w in word_lst:
                    if w == word:
                        print(f'[{word[0]}]{word[1:]}', end=' ')
                    else:
                        print(w, end=' ')
                print()
            break
    else:
        for i in range(len(words)):
            if words[i] != ' ' and not lst[ord(words[i].upper()) - 65]:
                lst[ord(words[i].upper()) - 65] = 1
                print(f'{words[:i]}[{words[i]}]{words[i + 1:]}')
                break
        else:
            print(words)
