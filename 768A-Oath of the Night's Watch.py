# https://codeforces.com/contest/768/problem/A

n = int(input())# number of stuards
a = sorted(list(map(int, input().split())))
max_el = a[-1]
min_el = a[0]
b = list(set(a))

count = 0 
if len(b) <= 2:
    count += 0
else:
    for i in range(n):
        if a[i] < max_el and a[i] > min_el:
            count += 1
            
print (count)
