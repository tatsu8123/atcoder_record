import copy

n = int(input())
colors = list(map(int,input().split()))
edge = [ [] for _ in range(n)]

for _ in range(n-1):
    a,b = map(int,input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

waiter = [(0,{colors[0]})]
ans = [0]
visited = set()
while len(visited)!=n:
    v,c = waiter.pop()
    if v in visited:
        continue
    visited.add(v)
    for next_v in edge[v]:
        if colors[next_v] in c:
            tmp = c.copy()
            waiter.append((next_v,tmp))
        else:
            tmp = c.copy()
            tmp.add(colors[next_v])
            waiter.append((next_v,tmp))
            ans.append(next_v)

ans.sort()
[ print(a+1) for a in ans]