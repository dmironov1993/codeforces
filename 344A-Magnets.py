# https://codeforces.com/problemset/problem/344/A

n = int(input())
a = []
for _ in range(n):
    a.append(input())

count = 0
for i in range(1,n):
    if a[i-1] != a[i]:
        count += 1
print (count + 1)
