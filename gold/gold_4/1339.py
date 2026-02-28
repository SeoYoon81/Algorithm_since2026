# 단어수학

n = int(input())
alph_dict = {}
for _ in range(n):
    word = list(input())
    l = len(word)
    for idx in range(l):
        pt = 10**(l - idx-1)
        if word[idx] in alph_dict:
            alph_dict[word[idx]] += pt
        else:
            alph_dict[word[idx]] = pt
num_lst = list(alph_dict.values())
num_lst.sort(reverse=True)
result = 0
for idx in range(len(num_lst)):
    result += num_lst[idx]*(9-idx)
print(result)