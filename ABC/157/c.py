n,m = map(int,input().split())
sc = [ list(map(int,input().split())) for _ in range(m)]

numbers = [0 for i in range(n)]
numbers[0] = 0 if n==1 else 1
flags = [ 0 for i in range(n)]

exist_flag = 1
for (s,c) in sc:
    if flags[s-1]==1 and numbers[s-1]!=c:
        exist_flag = 0
        break
    else:
        flags[s-1] = 1
        numbers[s-1] = c
exist_flag = 0 if numbers[0]==0 and n!=1  else exist_flag

num = 0
for idx,number in enumerate(numbers):
    num+=number*10**(n-1-idx)

ans =  num if exist_flag==1  else -1
print(ans) 