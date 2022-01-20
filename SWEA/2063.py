case = int(input())
num_list = list(map(int, input().split()))
print(sorted(num_list)[len(num_list)//2])