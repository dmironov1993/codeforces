# https://codeforces.com/contest/37/problem/A

n = int(input())
arr = list(map(int, input().split()))
m = max(arr) + 1
counts = [0]*m
for i in arr:
    counts[i] += 1
    
sub_list = []
for i in range(m):
    if i in arr:
        sub_list.append(counts[i])
sub_list.sort()

print (sub_list[-1], len(sub_list))
