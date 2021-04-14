n,m = map(int,input().split())
h = list(map(int,input().split()))

judge = [ 1 for i in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    if h[a-1]>h[b-1]:
        judge[b-1] = 0
    elif h[a-1]==h[b-1]:
        judge[a-1] = 0
        judge[b-1] = 0
    else:
        judge[a-1] = 0

ans = sum(judge)
print(ans)