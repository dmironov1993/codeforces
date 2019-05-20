# https://codeforces.com/problemset/problem/136/A

n = int(input())
p = list(map(int, input().split()))

ans = []
for i in range(1,n+1):
    ans.append(p.index(i)+1)
print (*ans)
