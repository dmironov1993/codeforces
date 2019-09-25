import math
n, b, d = map(int, input().split())
a = [*map(int, input().split())]

num = d
count = 0
for i in range(n):
    if a[i] <= b:
        num -= a[i]
    if num < 0:
        count += 1
        num = d
    
print (count)
