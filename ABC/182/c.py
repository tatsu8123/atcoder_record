n = input()

num = []
num_0 = 0
num_1 = 0
num_2 = 0
tot = 0
for c in n:
    tmp = int(c)
    rest = tmp%3
    tot = (tot+rest)%3
    if rest==0:
        num_0 += 0
    elif rest==1:
        num_1 += 1
    elif rest==2:
        num_2 += 1

if tot==0:
    ans = 0
elif tot==1:
    if num_1>=1:
        ans = 1 if len(n)>=2 else -1 
    elif num_2>=2:
        ans = 2 if len(n)>=3 else -1 
    else:
        ans = -1
elif tot==2:
    if num_2>=1:
        ans = 1 if len(n)>=2 else -1 
    elif num_1>=2:
        ans = 2 if len(n)>=3 else -1 
    else:
        ans = -1

print(ans)