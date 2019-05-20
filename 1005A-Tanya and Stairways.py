# https://codeforces.com/problemset/problem/1005/A

n = int(input())
a = list(map(int, input().split()))

idx = []
nums = []
for i in range(n):
    if a[i] == 1:
        idx.append(i)
        
for j in idx:
    if j != 0:
        nums.append(a[j-1])
nums.append(a[-1])
    
print (len(idx))
print (*nums)
