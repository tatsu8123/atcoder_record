x,y,z = map(int,input().split())

t_price = y/x
s_price = (t_price*z)//1 if t_price*z!=(t_price*z)//1 else (t_price*z)//1-1

print(int(s_price))