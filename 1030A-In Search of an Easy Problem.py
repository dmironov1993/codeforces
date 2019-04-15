# https://codeforces.com/problemset/problem/1030/A?locale=ru
# https://codeforces.com/contest/1030/submission/52775385

n = int(input())
a = list(map(int, input().split()))
level = 'EASY'
for el in a:
    if el == 1:
        level = 'HARD'
        print (level)
        break
if level == 'EASY':
    print (level)
