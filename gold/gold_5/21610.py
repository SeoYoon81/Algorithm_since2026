# 마법사 상어와 비바라기

import sys
input = sys.stdin.readline

# 구름 이동방향 
di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]

# 물복사용 대각선
di2=[-1, 1, 1, -1]
dj2=[1, -1, 1, -1]

n, m = map(int, input().split())
cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
map_mat = []
for _ in range(n):
    now_lst = list(map(int, input().split()))
    map_mat.append(now_lst)

for _ in range(m):
    d, s = map(int, input().split())
    # 일단 구름부터 이동 
    new_cloud = []
    for i, j in cloud:
        ni = (i + di[d-1] * s) % n
        nj = (j + dj[d-1] * s) % n
        new_cloud.append((ni, nj))
    cloud = new_cloud

    # 비내리기
    for i, j in cloud:
        map_mat[i][j] += 1

    # 물복사
    for i, j in cloud:
        cnt = 0
        for k in range(4):
            ni = i + di2[k]
            nj = j + dj2[k]
            if 0 <= ni < n and 0 <= nj < n:
                if map_mat[ni][nj] > 0:
                    cnt += 1
        map_mat[i][j] += cnt

    # 기존 구름 
    cloud_set = set(cloud)
    # 새 구름
    new_cloud = []
    for i in range(n):
        for j in range(n):
            if map_mat[i][j] >= 2 and (i, j) not in cloud_set:
                map_mat[i][j] -= 2
                new_cloud.append((i, j))
    cloud = new_cloud

print(sum(sum(i) for i in map_mat))