import math

n = int(input())
s = input()

r_num = s.count('R')
g_num = s.count('G')
b_num = s.count('B')

tot = r_num * g_num * b_num

for left in range(n):
    max_space = math.floor((n-3-left)//2)
    for space in range(max_space+1):
        center = left + space + 1
        right = center + space + 1
        if s[right]!=s[center] and s[center]!=s[left] and s[left]!=s[right]:
            tot -= 1

print(tot)