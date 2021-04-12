x = int(input())

flag = 0
for a in range(-118,120+1):
    for b in range(-119,120):
        if a**5-b**5==x:
            flag=1
            break
    if flag==1:
        break

print(a,b)