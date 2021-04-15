mod = 10**9 + 7
n,p = map(int,input().split())

ans = p-1
ans = (ans*pow(p-2,n-1,mod))%mod

print(ans)