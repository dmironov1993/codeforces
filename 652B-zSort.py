# https://codeforces.com/contest/652/problem/B

n = int(input())
arr = sorted(list(map(int, input().split())))
odd = [arr[i] for i in range(1,n,2)]
even = [arr[i] for i in range(0,n,2)]

ans = []
for i in range(1,n+1):
    if i % 2 != 0:
        ans.append(arr[0])
        arr.pop(0)
    else:
        ans.append(arr[-1])
        arr.pop(-1)
print (*ans)
