# https://codeforces.com/problemset/problem/231/A

n = int(input())

count = 0
for i in range(n):
    k = sum(tuple(map(int, input().split())))
    if k >= 2:
        count += 1
        
print (count)
