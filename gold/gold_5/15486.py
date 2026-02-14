#퇴사2

# 일단 dp구나...

import sys
input = sys.stdin.readline
t_lst = []
p_lst = []
n = int(input())
for _ in range(n):
    t, p = map(int, input().split())
    t_lst.append(t)
    p_lst.append(p)

dp = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    # 일정 문제로 안되는 것부터 처리
    if i + t_lst[i] > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], dp[i + t_lst[i]]+p_lst[i])
        
print(dp[i])