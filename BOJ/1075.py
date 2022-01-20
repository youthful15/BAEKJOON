N = int(int(input()) / 100) * 100 # 뒷자리를 00으로 만듦
F = int(input())
answer = 0

for i in range(100):
    if (N + i) % F == 0: # N + i가 F의 배수일 시 반복문 종료
        break

if i < 10:
    print(f'0{i}') # 10 미만일 시 앞에 0을 붙여 i를 출력
else:
    print(i) # 10 이상일 시 그냥 i를 출력
