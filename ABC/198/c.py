import math
r,x,y = map(int,input().split())

distance = math.sqrt(x**2+y**2)
if distance<r:
    ans = 2
elif distance >= r:
    ans = distance//r + 1 if distance%r!=0 else distance//r

print(int(ans))
