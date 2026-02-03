#LCS3
#lcs가 dp였으니까 dp일 것 같고....
# 문자열 3개니까 3차원 dp인가...

a = input()
b = input()
c = input()

dp = [[[0]*(len(c)+1) for _ in range(len(b)+1)] for _ in range(len(a)+1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        for k in range(1, len(c) + 1):
            if a[i-1] == b[j-1] == c[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(
                    dp[i-1][j][k],
                    dp[i][j-1][k],
                    dp[i][j][k-1]
                )

print(dp[len(a)][len(b)][len(c)])