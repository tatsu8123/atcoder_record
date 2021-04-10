n,k = map(int,input().split())
r,s,p = map(int,input().split())
t = input()

flag = [ 0 for i in range(n)]
score = 0

for idx,c in enumerate(t[:-k]):
    if c=='p' and flag[idx]==0:
        score+=s
        if idx+k<n and c==t[idx+k]:
            flag[idx+k]=1
    elif c=='r' and flag[idx]==0:
        score+=p
        if idx+k<n and c==t[idx+k]:
            flag[idx+k]=1
    elif c=='s' and flag[idx]==0:
        score+=r
        if idx+k<n and c==t[idx+k]:
            flag[idx+k]=1

for idx,c in enumerate(t[-k:]):
    if c=='p' and flag[idx+n-k]==0:
        score+=s
    elif c=='r' and flag[idx+n-k]==0:
        score+=p
    elif c=='s' and flag[idx+n-k]==0:
        score+=r

print(score)