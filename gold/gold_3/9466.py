# 텀 프로젝트

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def find_team(s, s_lst, visited, finished):
    visited[s] = True
    next_s = s_lst[s]
    count = 0
    # next_s 가 방문인 경우
    if visited[next_s]:
        # 팀 탐색 끝난 학생이면
        if finished[next_s]:
            pass
        else:
        # 팀 탐색 안 끝난 학생이면 사이클인거겠지
            now = next_s
            count += 1
            # 사이클 길이를 세자. 
            while now != s:
                now = s_lst[now]
                count += 1

    # next_s 가 방문 아닌 경우
    else: 
        # next_s에서 진행
        count += find_team(next_s, s_lst, visited, finished)
    finished[s] = True
    return count 


t = int(input())
for _ in range(t):
    n = int(input())
    s_lst =[0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    finished = [False] * (n + 1)
    count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            count += find_team(i, s_lst, visited, finished)

    print(n - count)

