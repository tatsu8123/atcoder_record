n,m = map(int,input().split())
A = set(list(map(int,input().split())))
B = set(list(map(int,input().split())))
a_and_b = A & B
a_or_b = (A|B) - a_and_b

ans = list(a_or_b)
ans.sort()
ans = [ str(a) for a in ans]
print(' '.join(ans))
