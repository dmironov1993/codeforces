# https://codeforces.com/contest/230/problem/A

s,n = tuple(map(int, input().split()))

game_sets = sorted([tuple(map(int, input().split())) for _ in range(n)])

outcome = 'YES'
for i in range(n):
    if s > game_sets[i][0]:
        s += game_sets[i][1]
    else:
        outcome = 'NO'
        break
print (outcome)
