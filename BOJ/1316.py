case = int(input())
answer = case

for i in range(case):
    word = input()
    wordlist = list(set(word))
    worddict = {}
    for i in range(len(wordlist)): #알파벳 키의 빈 딕셔너리 생성
        worddict[wordlist[i]] = []
    
    for j in range(len(word)): #딕셔너리 밸류로 위치값 집어넣음
        for k in range(len(wordlist)):
            if word[j] == wordlist[k]:
                worddict[wordlist[k]].append(j)
    
    mang = 0
    
    for abc in wordlist: #위치값이 이어지지 경우 망한 단어
        if len(worddict[abc]) > 1 :
            for i in range(len(worddict[abc])-1) :
                if worddict[abc][i] + 1 != worddict[abc][i+1]:
                    mang = 1
        
    answer -= mang # 전체 단어 - 망한 단어
        
print(answer)