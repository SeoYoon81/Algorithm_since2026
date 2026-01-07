#랜선 자르기
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan_lst = []
for _ in range(k):
    x = int(input())
    lan_lst.append(x)

# 길이 now_len인 것으로 나오는 랜선의 수 구하는 함수
def count_lan(lst, now_len):
    cnt = 0
    for x in lst:
        cnt += x//now_len
    return cnt

# 랜선 길이 후보 범위 
min_len = max(1, sum(lan_lst)//(n + k)) #zero division error 예방
max_len = sum(lan_lst)//n

now_lan = (min_len + max_len) // 2

#일단 now_lan을 n개 나오도록 해보자
now_cnt = count_lan(lan_lst, now_lan)

while  max_len - min_len >= 2:
    # 갯수가 많거나 같으면 길이 긴 쪽에서 뒤지고
    if now_cnt >= n:
        min_len = now_lan
    # 갯수가 적으면 길이 짧은 쪽에서 뒤지기
    if now_cnt < n:
        max_len = now_lan
    # now_cnt 리셋도 잊지 않기 
    now_lan = (max_len + min_len)//2
    now_cnt = count_lan(lan_lst, now_lan)
    # print(min_len, now_lan, max_len)


# 혹시 모르니까 max_len도 확인하기
if count_lan(lan_lst, max_len) == n:
    print(max_len)
else:
    print(now_lan)