# https://codeforces.com/problemset/problem/935/A

n = int(input())

count = 0
for i in range(1,n):
    if n % i == 0:
        count += 1
print (count)