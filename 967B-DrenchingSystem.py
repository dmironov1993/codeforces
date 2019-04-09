# https://codeforces.com/contest/967/problem/B

n, A, B = tuple(map(int, input().split()))
s = list(map(int, input().split()))

diff = sum(s) - s[0]*A/B
s.pop(0)
s.sort()

count = 0
summa = 0
for i in range(1,len(s)+1):
    if diff <= 0:
        break
    else:
        summa += s[-i]
        count += 1
        if summa >= diff:
            break
        
print (count)
