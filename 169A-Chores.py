# https://codeforces.com/contest/169/problem/A
# https://codeforces.com/contest/169/submission/52562524

n, a, b = tuple(map(int, input().split()))
h = sorted(list(map(int, input().split())))

status = None
Peter = h[-a:]
diff = h[-a] - h[-a-1]
if diff == 0:
    status = 0
else:
    status = diff
print (status)
