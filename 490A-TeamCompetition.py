# https://codeforces.com/contest/490/problem/A

n = int(input())
t = list(map(int, input().split()))

idx1 = []
for i in range(len(t)):
    if t[i] == 1:
        idx1.append(t.index(1, i))
        
idx2 = []
for i in range(len(t)):
    if t[i] == 2:
        idx2.append(t.index(2,i))
        
idx3 = []
for i in range(len(t)):
    if t[i] == 3:
        idx3.append(t.index(3,i))
        
arr = [len(idx1), len(idx2), len(idx3)]
min_arr = min(arr)
idx1 = idx1[:min_arr]
idx2 = idx2[:min_arr]
idx3 = idx3[:min_arr]
indices = [[i+1,j+1,k+1] for i,j,k in zip(idx1, idx2, idx3)]

print (len(indices))
if len(indices) != 0:
    for k in range(len(indices)):
        print (*indices[k])
