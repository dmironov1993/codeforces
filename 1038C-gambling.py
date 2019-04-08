# https://codeforces.com/problemset/problem/1038/C

n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
b = sorted(list(map(int, input().split())), reverse=True)

score_a = 0
score_b = 0
step = 'a'
empty = False
while not empty:
    if a != [] and b != []:
        if step == 'a' and a[0] > b[0]:
            score_a += a[0]
            a.pop(0)
            step = 'b'
        elif step == 'a' and a[0] <= b[0]:
            b.pop(0)
            step = 'b'
        elif step == 'b' and a[0] >= b[0]:
            a.pop(0)
            step = 'a'
        elif step == 'b' and b[0] > a[0]:
            score_b += b[0]
            b.pop(0)
            step = 'a'
    else:
        if step == 'b' and b == []:
            a.pop(0)
            step = 'a'
        elif step == 'a' and a == []:
            b.pop(0)
            step = 'b'
        elif step == 'a' and b == []:
            score_a += a[0]
            a.pop(0)
            step = 'b'
        elif step == 'b' and a == []:
            score_b += b[0]
            b.pop(0)
            step= 'a'
        
    if a == [] and b == []:
        empty = True
        
print (score_a - score_b)
