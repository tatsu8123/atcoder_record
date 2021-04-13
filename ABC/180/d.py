from math import log

x,y,a,b = map(int,input().split())

exp = 0
border = min(b//(a-1),y-1)

if x>border:
    exp += (y-1-x)//b
elif x<=border:
    mul_num = int(log((border/x),a))
    x = x*a**(mul_num)
    exp += mul_num
    exp += (y-1-x)//b

print(exp)