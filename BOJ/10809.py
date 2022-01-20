# a = list(input())
# alpha = [-1 for i in range(26)]
# # 알파벳 26개 리스트를 -1로 초기화

# for i in a:
#     if alpha[ord(i) - 97] == -1:
#         alpha[ord(i) - 97] = a.index(i)
# # 해당 알파벳의 위치 값이 -1일 경우 현재 인덱스 값으로 변경

# for i in alpha:
#     print(i,end=' ')

a = input()
alpha = list(range(26))

for i in range(26):
    print(a.find(chr(97 + i)),end=' ')