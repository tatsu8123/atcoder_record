a,b = map(int,input().split())

max_num = 0
for num in range(1,b-a+1):
    small = (a//num) * num if a%num==0 else  ((a//num)+1) * num
    large = ((a//num)+1) * num if a%num==0 else  ((a//num)+2) * num
    if a<=small<=b and a<=large<=b:
        max_num = num

print(max_num)