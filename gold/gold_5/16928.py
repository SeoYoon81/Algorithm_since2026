#뱀과 사다리 게임

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

# 근데 이거 뱀/사다리 구분할 필요가 있나...?
s_dict = {}
for _ in range(n + m):
    a, b = map(int, input().split())
    s_dict[a] = b

# 각 번호까지 가는 최소 횟수를 저장하는 리스트, idx 편의상 그냥 앞에 빈 0 붙임
step_lst = [-1 for _ in range(101)]
step_lst[0] = 0
step_lst[1] = 0

target = deque([1])
# 각 target에 대해, 1~6까지를 기록 
while target:
    now = target.popleft()
    if now == 100:
        break
    now_step = step_lst[now]
    for i in range(1, 7):
        nxt = now + i
        if nxt > 100:
            continue
        if nxt in s_dict:
            nxt = s_dict[nxt]
        # 방문했으면 건너뛰기
        if step_lst[nxt] == -1:
            step_lst[nxt] = step_lst[now] + 1
            target.append(nxt)
print(step_lst[100])