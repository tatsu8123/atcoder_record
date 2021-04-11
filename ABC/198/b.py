s = input()
s_list = [ c for c in s]
s_list.reverse()

new_s = []
for idx,c in enumerate(s_list):
    if c!='0':
        new_s = s_list[idx:]
        break

ans = 'Yes'
for idx in range(len(new_s)//2):
    if new_s[idx]!=new_s[-1-idx]:
        ans = 'No'
        break

print(ans)