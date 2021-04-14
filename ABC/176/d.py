from collections import deque

def bfs(start_y,start_x,area,field,height,width):
    que = deque()
    que.append((start_y,start_x))
    field[start_y][start_x] = 0
    visited_points = set()

    while len(que):
        y,x = que.popleft()

        if area[y][x] == '#':
            continue
        elif (y,x) in visited_points:
            continue

        visited_points.add((y,x))
        current_cost = field[y][x]

        for delta in [-1,1]:
            if 0<=y+delta<height:
                que.appendleft((y+delta,x))
                field[y+delta][x] = min(current_cost,field[y+delta][x])
        
        for delta in [-1,1]:
            if 0<=x+delta<width:
                que.appendleft((y,x+delta))
                field[y][x+delta] = min(current_cost,field[y][x+delta])


        for x_delta in range(-2,3):
            if 0<=x+x_delta<width:
                for y_delta in range(-2,3):
                    if 0<=y+y_delta<height:
                        que.append((y+y_delta,x+x_delta))
                        field[y+y_delta][x+x_delta] = min(current_cost+1,field[y+y_delta][x+x_delta])

    return field

h,w = map(int,input().split())
ch,cw = map(int,input().split())
dh,dw = map(int,input().split())
pseudo_max = 10**6

area = []
for height in range(h):
    row = input()
    area.append(row)
field = [ [pseudo_max for _ in range(w)] for _ in range(h)]

field = bfs(ch-1,cw-1,area,field,h,w)
ans = field[dh-1][dw-1] if field[dh-1][dw-1]!=pseudo_max else -1
print(ans)