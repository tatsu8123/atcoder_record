from collections import Counter

N = int(input())
ss = []
for _ in range(N):
    tmp = input()
    ss.append(tmp)

c = Counter(ss)
sorted_ss = c.most_common()
max_appearance = sorted_ss[0][1]

ans = []
for (s,tmp_num) in sorted_ss:
    if tmp_num != max_appearance:
        break
    else:
        ans.append(s)

ans.sort()
[ print(s) for s in ans]