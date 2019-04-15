# https://codeforces.com/problemset/problem/1136/A
# https://codeforces.com/contest/1136/submission/52777794


n = int(input())
l = []
r = []
for _ in range(n):
    arr = list(map(int, input().split()))
    l.append(arr[0])
    r.append(arr[1])
k = int(input())
i = 0
while True:
    if r[i] >= k:
        print (len(r[i:]))
        break
    else:
        i += 1
