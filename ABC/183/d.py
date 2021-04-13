n,w = map(int,input().split())

time_scheme = []
for _ in range(n):
    s,t,p = map(int,input().split())
    time_scheme.append((s,p))
    time_scheme.append((t,-1*p))

time_scheme.sort()

previous = -1
water = 0
ans = 'Yes'
for (time,p) in time_scheme:
    if previous!=time:
        if water>w:
            ans = 'No'
            break
        previous = time

    water += p


print(ans)