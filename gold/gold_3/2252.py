#줄세우기

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range( n + 1)]
degree = [0 for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

target = deque([])
for i in range(1, n + 1):
    if degree[i] == 0:
        target.append(i)
answer = []
while target:
    now = target.popleft()
    answer.append(now)
    for x in graph[now]:
        degree[x] -= 1
        if degree[x] == 0:
            target.append(x)
print(*answer)

