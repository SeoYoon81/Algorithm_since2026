#나머지 합

# 누적합의 나머지 기록, 같은 것끼리 묶어서 2개 선택하는 경우의 수
# 생가해보니 기록도 아니고 각 나머지가 몇 개씩인지만 세면 됨

n, m = map(int, input().split())
num_lst = list(map(int, input().split()))
# 각 나머지를 기록할 dict 초기값 0인거 고려해서 0:1로 시작하기
q_dict = {0 : 1}
for i in range(1, m):
    q_dict[i] = 0

now_sum = 0
for x in num_lst:
    now_sum = (now_sum + x) % m
    q_dict[now_sum]+= 1

cnt = 0
for idx in range(m):
    a = q_dict[idx]
    # a 개 중 2개를 고르는 경우의 수
    cnt += a * (a - 1) // 2

print(cnt)
