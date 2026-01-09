#LCA
import sys
input = sys.stdin.readline
from collections import deque


# 트리 입력
n = int(input())
tree_dict = {i : set() for i in range(1, n + 1)}

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree_dict[a].add(b)
    tree_dict[b].add(a)

# 1을 시작점으로, 부모 노드와 depth 기록
parent_lst = [0 for _ in range(n + 1)]
parent_lst[1] = 1
depth_lst = [0 for _ in range(n + 1)]
target = deque([1])
while target:
    now_node = target.popleft()
    for x in tree_dict[now_node]:
        if parent_lst[x]:
            continue
        parent_lst[x] = now_node
        depth_lst[x] = depth_lst[now_node] + 1
        target.append(x)

# 시간 단축 위한 전처리
max_depth = max(depth_lst)
LOG = max_depth.bit_length()
parent = [parent_lst]
for k in range(1, LOG):
    prev = parent[-1]
    cur = [0 for _ in range(n + 1)]
    for x in range(1, n + 1):
        cur[x] = prev[prev[x]]
    parent.append(cur)

# 가까운 공통조상 찾는 함수
def find_parent(a, b):
    # depth 맞추기
    if depth_lst[a]<depth_lst[b]:
        a, b = b, a
    
    dif = depth_lst[a] - depth_lst[b]
    for k in range(LOG):
        if dif &(1<<k):
            a = parent[k][a]

    if a == b:
        return a
    # 같은 놈 나올 때까지
    for k in range(LOG - 1, -1, -1):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]
    return(parent[0][a])



# 정점 쌍
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    ans = find_parent(a, b)
    print(ans)
