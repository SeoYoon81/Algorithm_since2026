# # 골드바흐 파티션
# # 일단 소수 셋부터 만들어보자 

# num_lst = [False for _ in range(2)] + [True for _ in range(999999)]
# for i in range(1000001):
#     # 소수일 때, i의 배수를 False로 바꾸자
#     if num_lst[i]:
#         for k in range(2, 1000000//i + 1):
#             num_lst[k*i] = False

# prime_lst = [i for i in range(1000000) if num_lst[i]]
# t = int(input())

# for _ in range(t):
#     n = int(input())
#     cnt = 0
#     idx = 0
#     while prime_lst[idx] < n//2 + 1:
#         # 골드바흐 추측 성립하면 cnt+ 1
#         if n-prime_lst[idx] in prime_lst:
#             cnt += 1
#         idx += 1
#     print(cnt)
# 골드바흐 파티션
# 일단 소수 셋부터 만들어보자 

t = int(input())
case_lst = []
for _ in range(t):
    n = int(input())
    case_lst.append(n)

max_num = max(case_lst)
num_lst = [False for _ in range(2)] + [True for _ in range(max_num - 1)]
for i in range(2, int(max_num**0.5) + 1):
    # 소수일 때, i의 배수를 False로 바꾸자
    if num_lst[i]:
        for k in range(i, max_num//i + 1):
            num_lst[k*i] = False

prime_lst = [i for i in range(len(num_lst)) if num_lst[i]]
prime_set = set(prime_lst)
for x in case_lst:
    cnt = 0
    idx = 0
    while prime_lst[idx] < x//2 + 1:
        # 골드바흐 추측 성립하면 cnt+ 1
        if x-prime_lst[idx] in prime_set:
            cnt += 1
        idx += 1
    print(cnt)
