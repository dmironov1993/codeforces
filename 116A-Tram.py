# https://codeforces.com/problemset/problem/116/A?locale=en

n = int(input())

c = []
c.append(0)
for i in range(n):
    a,b = tuple(map(int, input().split()))
    c.append(c[i] - a + b)
print (max(c))
