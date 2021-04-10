n = int(input())
a = list(map(int,input().split()))

mod = 10**9+7

a.reverse()
cumsum = [0]
for num in a[:-1]:
    cumsum.append(cumsum[-1]+num)

tot = 0
a.reverse()
cumsum.reverse()
for num,c_sum in zip(a,cumsum):
    tmp = (num*c_sum) % mod
    tot = (tot+tmp) % mod

print(tot)