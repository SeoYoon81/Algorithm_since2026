# 게임

x, y = map(int, input().split())

z = (100 * y)//x

if z == 99 or z == 100:
    print(-1)
else:
    answer = ((z + 1) * x - 100 * y - 1) // (99 - z)
    print(answer + 1)