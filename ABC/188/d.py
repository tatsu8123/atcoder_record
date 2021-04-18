n,subscribe = map(int,input().split())

days = []
for num in range(n):
    a,b,c = map(int,input().split())
    days.append((a,c))
    days.append((b+1,-1*c))

days.sort()
prev = 1
tmp_cost = 0
tot_cost = 0
for (day,cost) in days:
    if day!=prev:
        tot_cost += (day-prev)*min(tmp_cost,subscribe)
    
    prev = day
    tmp_cost += cost


print(tot_cost)