# 사다리 조작

import sys
input= sys.stdin.readline
n, m, h = map(int, input().split())
# 사다리 전체에서 가로선 유무 기록
ladder = [[False for _ in range(n + 1)] for _ in range(h + 1)]
for _ in range(m):
    y, x = map(int, input().split())
    ladder[y][x] = True

# 횟수 제한이 3이라는 것이 포인트 아닐까...
# 힌트를 보면 추가되는 선이 꼭 아래에 있어야 하는 건 아님

# n 개의 수를 n 자리에 배열하는데 순열로 접근할수는 없을까 
# 우선 항등순열 여부부터 판단해보자
def check(now_lst):
    length = len(now_lst)
    flag = True
    for s in range(1, length ):
        if now_lst[s] == s:
            continue
        else:
            flag = False
            break
    return flag

def last_lst():
    P = [0] * (n + 1)
    for start in range(1, n + 1):
        cur = start
        for y in range(1, h + 1):
            if cur <= n - 1 and ladder[y][cur]:
                cur += 1
            elif cur > 1 and ladder[y][cur - 1]:
                cur -= 1
        P[start] = cur
    return P


# 가로선을 최대 3개까지 추가하며 탐색
def dfs(cnt, start_y, start_x, limit):
    # 현재 사다리 상태가 항등 순열이면 성공
    if check(last_lst()):
        return True
    # 가로선 3개 초과하면 실패
    if cnt == limit:
        return False

    for y in range(start_y, h + 1):
        x_begin = start_x if y == start_y else 1
        for x in range(x_begin, n):
            # 가로선 추가 가능 여부 검사
            if ladder[y][x]:
                continue
            if x > 1 and ladder[y][x - 1]:
                continue
            if x < n - 1 and ladder[y][x + 1]:
                continue

            # 가로선 추가 (인접 swap 추가)
            ladder[y][x] = True
            if dfs(cnt + 1, y, x + 1, limit):
                return True
            ladder[y][x] = False

    return False


# 정답 탐색
answer = -1
for i in range(4):  # 0, 1, 2, 3
    if dfs(0, 1, 1, i):
        answer = i
        break

print(answer)