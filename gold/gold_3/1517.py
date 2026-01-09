# 욕심쟁이 판다

import sys
input = sys.stdin.readline
from collections import deque

#입력
n = int(input())
bamboos = []
for _ in range(n):
    cur = list(map(int, input().split()))
    bamboos.append(cur)

parent_lst = [[] for _ in range(n*n )]
child_lst = [[] for _ in range(n * n)]
dir = [-n, -1, 1, n]
for k in range(n * n):
    now_bamboo = bamboos[k//n][k%n]
    for d in dir:
        #예외처리
        if k+d < 0 or k + d >= n*n:
            continue
        # 양이 더 많으면 child_lst로,
        # 적으면 par_lst로 
        next_bamboo = bamboos[(k+d)//n][(k+d)%n]
        if next_bamboo>now_bamboo:
            child_lst[k].append(k + d)
        if next_bamboo < now_bamboo:
            parent_lst[k].append(k + d)

start_lst = [i for i in range(n * n) if parent_lst[i] == []]
depth_lst = [0 for _ in range(n*n)]
for x in start_lst:
    depth_lst[x] = 1

target = deque(start_lst)
while target:
    now_node = target.popleft()
    now_depth = depth_lst[now_node]
    for x in child_lst[now_node]:
        depth_lst[now_node] = now_depth + 1
        target.append(x)
print(max(depth_lst))