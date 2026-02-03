# BFS (Breadth-First Search)

## 기본 개념
- 큐(Queue)를 사용한 레벨 단위 탐색
- 최단 거리 문제에 적합

## 기본 코드 패턴
```python
from collections import deque

def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
