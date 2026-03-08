#구슬탈출

import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
n, m = map(int,input().split())
board = []
for _ in range(n):
    row = list(input().strip())
    board.append(row)