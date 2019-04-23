https://codeforces.com/contest/1107/problem/B

n = int(input())
k, x = [], []
for _ in range(n):
    arr = list(map(int, input().split()))
    k.append(arr[0])
    x.append(arr[1])
    
for j in range(n):
    print (9*k[j] - (9-x[j]))
