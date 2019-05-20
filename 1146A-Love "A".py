# https://codeforces.com/problemset/problem/1146/A?locale=ru

s = input()
n = len(s)

count = 0
for i in range(n):
    if s[i] == 'a':
        count += 1
other = n-count        
if count > other:
    print (n)
elif count == other:
    print (n-1)
else:
    print (2*count-1)
