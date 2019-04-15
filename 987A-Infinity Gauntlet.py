# https://codeforces.com/problemset/problem/987/A
# https://codeforces.com/contest/987/submission/52776804

n = int(input())

dct = {'purple': 'Power',
       'green': 'Time',
       'blue': 'Space',
       'orange': 'Soul',
       'red': 'Reality',
       'yellow': 'Mind'}
       
colors_has = []
for _ in range(n):
    colors_has.append(input())
    
print (6-n)
doesnot_have = list(set(dct.keys()) - set(colors_has))
for i in range(6-n):
    print (dct[doesnot_have[i]])
