# https://codeforces.com/problemset/problem/677/A?locale=ru


n,h=tuple(map(int,input().split()))
a = list(map(int,input().split()))

w = []
for i in range(n):
    if a[i] > h:
        w.append(2)
    else:
        w.append(1)
        
print (sum(w))
