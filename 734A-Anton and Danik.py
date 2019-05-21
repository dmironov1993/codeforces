# https://codeforces.com/problemset/problem/734/A

n = int(input())
s = list(input())

count_a = 0
count_d = 0
for i in range(n):
    if s[i] == 'D':
        count_d += 1
    else:
        count_a += 1
if count_a == count_d:
    print ('Friendship')
elif count_a > count_d:
    print ('Anton')
else:
    print ('Danik')
