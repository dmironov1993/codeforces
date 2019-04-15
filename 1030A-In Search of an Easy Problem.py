# https://codeforces.com/problemset/problem/1030/A?locale=ru

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
