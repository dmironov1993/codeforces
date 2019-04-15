# https://codeforces.com/problemset/problem/785/A

dct = {'Tetrahedron':4,
       'Cube':6,
       'Octahedron':8,
       'Dodecahedron':12,
       'Icosahedron':20}

n = int(input())
s = []
count = 0
for _ in range(n):
    s.append(input())
for i in range(n):
    name = s[i]
    count += dct[name]
print(count)
