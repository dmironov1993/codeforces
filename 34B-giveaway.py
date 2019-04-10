https://codeforces.com/contest/34/problem/B

n, m = tuple(map(int, input().split()))
a = sorted(list(map(int, input().split())))

amount = 0
for i in range(m):
    if a[i] < 0:
        amount += abs(a[i])
    else:
        continue
print (amount)
