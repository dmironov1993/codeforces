# https://codeforces.com/problemset/problem/149/A

k = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
count = 0
if k != 0:
    for i in range(len(a)):
        k = k - a[i]
        count += 1
        if k <= 0:
            break

if k > 0:
    print (-1)
else:
    print (count)
