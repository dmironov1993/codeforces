# https://codeforces.com/contest/701/problem/B


n, m = tuple(map(int, input().split()))

x = set()
y = set()
res = []
for i in range(m):
    a,b = tuple(map(int, input().split()))
    x.add(a)
    y.add(b)
    res.append(n**2-(n*len(x) + n*len(y)-len(x)*len(y)))
print (*res)
