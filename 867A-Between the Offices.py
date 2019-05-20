# https://codeforces.com/problemset/problem/867/A?locale=ru

n = int(input())
a = list(input())

count_s = 0
count_f = 0
for i in range(n-1):
    if a[i] == 'S' and a[i] != a[i+1]:
        count_s += 1
    elif a[i] == 'F' and a[i] != a[i+1]:
        count_f += 1
        
if count_s > count_f:
    print ('YES')
else:
    print ('NO')
