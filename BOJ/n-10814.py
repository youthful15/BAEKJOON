case = int(input())
# age_list = [0 for i in range(case)]
# name_list = [0 for i in range(case)]

# for i in range(case):
#     age_list[i], name_list[i] = input().split()
    
# for i in range(int(min(age_list)), int(max(age_list)) + 1):
#     for j in range(case):
#         if i == int(age_list[j]):
#             print(age_list[j], name_list[j])

case_list = [0 for i in range(case)]

for i in range(case):
    case_list[i] = list(input().split())
    
lam_list = sorted(case_list, key = lambda x: x[0])

for i in range(len(lam_list)):
    print(lam_list[i][0], lam_list[i][1])