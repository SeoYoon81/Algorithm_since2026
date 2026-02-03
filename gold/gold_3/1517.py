# 욕심쟁이 판다

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
bamboo = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]

    dp[x][y] = 1
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if bamboo[nx][ny] > bamboo[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))

print(ans)
