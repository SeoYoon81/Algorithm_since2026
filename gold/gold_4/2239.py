#스도쿠

#입력값부터 받자
board = []
for _ in range(9):
    n = list(input())
    board.append(n)

#사전순 배열이니까 set 사용은 안될 듯
#숫자는 숫자칸으로, 0은 위치 기록 + 리스트로
gaiming_board=[[0 for _ in range(9)] for _ in range(9)]
blank_lst = []
for i in range(9):
    for j in range(9):
        if board[i][j] == '0':
            # idx 다루기 편하게 하려고 그냥 10개로 만들었음
            gaiming_board[i][j] = [0]+[1 for _ in range(9)]
            blank_lst.append((i,j))
        else:
            gaiming_board[i][j] = int(board[i][j])

# 이제 1차적으로 걸르기
for i in range(9):
    for j in range(9):
        if isinstance(gaiming_board[i][j], int):
            now_num = gaiming_board[i][j]
            for k in range(9):
                if isinstance(gaiming_board[i][k], list):
                    gaiming_board[i][k][now_num]=0
                if isinstance(gaiming_board[k][j], list):
                    gaiming_board[k][j][now_num]=0
                if isinstance(gaiming_board[(i//3)*3+ k//3][(j//3)*3+k%3], list):
                    gaiming_board[(i//3)*3+ k//3][(j//3)*3+k%3][now_num]=0

# idx번째 빈 칸에 넣을 숫자와, 그 숫자로 인해 후보가 제외된 빈칸들
solving_stack = []
l = len(blank_lst)
flag = False
def solve(idx):
    global flag
    if flag: return
    # 다 찼으니까 성공 - 끝
    if idx == l:
        flag = True
        return 
    i, j = blank_lst[idx]
    if sum(gaiming_board[i][j][1:]) == 0:
        return 
    # 후보 제외
    for num in range(1, 10):
        # 0인건 불가능한 거니까 패스
        if not gaiming_board[i][j][num]:
            continue
        # 1이면 해당 숫자 넣고 그걸로 인해 후보 제거된 칸 기록
        delete_lst = []

        # 현재 후보 상태 임시 저장
        original_candidates = gaiming_board[i][j][:]
        # 현재 칸 넣어둠
        gaiming_board[i][j] = num
        # 영향받는 칸들 중 후보 리스트에서 더 뒤에 있는 것들에만 후보 삭제
        for k in range(9):
            if isinstance(gaiming_board[i][k], list):
                # 후보로 있으면 제외하고, delete_lst에 넣기
                if gaiming_board[i][k][num]:
                    gaiming_board[i][k][num]=0
                    delete_lst.append((i, k))
            if isinstance(gaiming_board[k][j], list):
                if gaiming_board[k][j][num]:
                    gaiming_board[k][j][num]=0
                    delete_lst.append((k, j))
            if isinstance(gaiming_board[(i//3)*3+ k//3][(j//3)*3 + k % 3], list):
                if gaiming_board[(i//3)*3 + k//3][(j//3)*3 + k%3][num]:
                    gaiming_board[(i//3)*3+ k//3][(j//3)*3 + k%3][num]=0
                    delete_lst.append(((i//3)*3 + k//3, (j//3)*3 + k%3))
        # 최적화 _ 스택 기록 전에 미리 가지치기
        for a, b in delete_lst:
            # 그걸로 인해 후보 제외된 애가 있다면 
            if not sum(gaiming_board[a][b]):
                # 스택에 입력 안하고 다음 단계
                for x, y in delete_lst:
                    gaiming_board[x][y][num]= 1
                # gaiming_board도 복구
                gaiming_board[i][j] = original_candidates
                break
        else:
            # 입력 num, 삭제사항 스택에 기록        
            solving_stack.append((num, delete_lst))  
            # 다음 idx 탐색
            solve(idx+1)
            if flag:
                return
            # 복구
            save_num, save_lst = solving_stack.pop()
            # save_lst 돌면서 save_num 복구
            for a, b in save_lst:
                gaiming_board[a][b][save_num]=1
            gaiming_board[i][j] = original_candidates

# print(len(blank_lst))
solve(0)
# print(solving_stack)

#이제 정답 출력하자
for i in range(9):
    i_str = ''
    for x in gaiming_board[i]:
        i_str += str(x)
    print(i_str)




