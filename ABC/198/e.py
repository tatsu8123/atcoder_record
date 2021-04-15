import sys
sys.setrecursionlimit(10**6)

def dfs(current_node):
    visited[current_node]=True
    color_flag[colors[current_node]] += 1
    if color_flag[colors[current_node]]==1:
        ans.append(current_node)
    for next_node in edge[current_node]:
        if visited[next_node] == True:
            continue
        dfs(next_node)

    color_flag[colors[current_node]] -= 1


n = int(input())
colors = list(map(int,input().split()))
colors = [ num-1 for num in colors]
edge = [ [] for _ in range(n)]

for _ in range(n-1):
    a,b = map(int,input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

color_flag = [ 0 for _ in range(10**6)]
ans = []
visited = [ False for _ in range(n)]
dfs(0)

ans.sort()
[ print(a+1) for a in ans]


## TLE取れなかったdfs(while)
# waiter = [(0,{colors[0]})]
# ans = [0]
# visited = set()
# while  len(visited)!=n:
#     v,c = waiter.pop()
#     visited.add(v)
#     for next_v in edge[v]:
#         if next_v in visited:
#             continue
#         elif colors[next_v] in c:
#             tmp = c.copy()
#             waiter.append((next_v,tmp))
#         else:
#             tmp = c | {colors[next_v]}
#             waiter.append((next_v,tmp))
#             ans.append(next_v)
#
# ans.sort()
# [ print(a+1) for a in ans]
