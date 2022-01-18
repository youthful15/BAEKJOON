a = str(input())
b = list('CAMBRIDGE')
for i in b:
    # replace 메소드로 CAMBRIDGE 각 알파벳을 제거
    a = a.replace(i,'')
print(a)

