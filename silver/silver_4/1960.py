#에라토스테네스의 체

n, k = map(int, input().split())
num_lst = [False] * (n + 1)
comb_lst = []
for i in range(2, n + 1):
    if num_lst[i]:
        continue
    for j in range(1, n//i + 1 ):
        if not num_lst[i*j]:
            num_lst[i*j] = True
            comb_lst.append(i * j)

print(comb_lst[k - 1])