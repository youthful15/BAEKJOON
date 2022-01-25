case = int(input())
word_list = [0 for i in range(case)]

for i in range(case):
    word_list[i] = input()
    
new_words = sorted(list(set(word_list))) #중복값 제거 후 정렬
word_nums = [0 for i in range(len(new_words))]

for i in range(len(new_words)):
    word_nums[i] = len(new_words[i]) #동일한 인덱스에 길이 추가

for i in range(1, max(word_nums) + 1):
    for j in range(len(word_nums)): #길이가 짧은 단어부터 정렬된 순대로 출력
        if word_nums[j] == i:
            print(new_words[j])