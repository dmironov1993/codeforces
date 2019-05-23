# https://codeforces.com/problemset/problem/236/A?locale=en

s = list(input())
n = len(s)

dct = {}
for i in range(n):
    if s[i] not in dct.keys():
        dct[s[i]] = 1
    else:
        dct[s[i]] += 1

k = len(dct.keys())
if k % 2 == 0:
    print ("CHAT WITH HER!")
else:
    print ('IGNORE HIM!')
