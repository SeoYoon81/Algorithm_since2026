# 가장 긴 감소하는 부분수열

n = int(input())
lst = list(map(int, input().split()))

# 일단 dp인건 알겠어....
len_lst = [0 for _ in range(n)]
len_lst[0] = 1
# 리스트 순회하며 거기까지의 가장 긴 감소부분수열 기록
for i in range(1, n):
    max_len = 0
    # 현위치까지 순회하며, 나보다 큰 놈 중 가장 긴 감소수열 + 1
    for j in range(n):
        if lst[j] > lst[i]:
            max_len = max(max_len, len_lst[j])
    len_lst[i] = max_len + 1
print(max(len_lst))
