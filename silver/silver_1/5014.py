#스타트링크

# bfs
from collections import deque

f, s, g, u, d = map(int, input().split())
building = [-1 for _ in range(f + 1) ]
building[s] = 0
target = deque([s])

while target:
    # 일단 g가 차면 바로 break 
    if building[g] != -1:
        break
    now_f = target.popleft()
    c = building[now_f]
    if 0<= now_f + u <= f:
        if building[now_f + u] == -1:
            building[now_f + u] = c + 1
            target.append(now_f+u)
    if 0< now_f - d<=f:
        if building[now_f-d] == -1:
            building[now_f - d]= c + 1
            target.append(now_f-d)


#탐색 완료 후 결과 출력
if building[g] == -1:
    print("use the stairs") 
else:
    print(building[g])