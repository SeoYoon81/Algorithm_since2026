#앱
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memory_lst = list(map(int, input().split()))
cache_lst = list(map(int, input().split()))

max_cost = sum(cache_lst)
dp = [0] * (max_cost + 1)

for i in range(n):
    mem = memory_lst[i]
    cost = cache_lst[i]
    for c in range(max_cost, cost - 1, -1):
        dp[c] = max(dp[c], dp[c - cost] + mem)

for c in range(max_cost + 1):
    if dp[c] >= m:
        print(c)
        break
