# https://codeforces.com/contest/174/problem/A

n, b = tuple(map(int, input().split()))
a = list(map(int, input().split()))

maximum = max(a)
d = []
for i in range(n):
    diff = maximum - a[i]
    if b >= diff:
        d.append(a[i] + diff)
        b -= diff
el = d[0]
res = 'ok'
for j in d:
    if j != el:
        res = 'not ok'
add = 0
if len(d) != len(a):
    res = 'not ok'
else:
    add += b / len(d)
#    b -= b
if res == 'ok':
    ans = [i-j for i,j in zip(d,a)]
    for k in range(n):
        ans[k] += add
        if type(ans[k]) == int:
            print ('{:.6f}'.format(ans[k]))
        else:
            print (ans[k])
else:
    print (-1)
