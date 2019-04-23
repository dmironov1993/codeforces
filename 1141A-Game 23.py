# https://codeforces.com/contest/1141/problem/A

n, m = tuple(map(int, input().split()))
num1 = m/n
a = []
while True:
    if num1 % 2 == 0:
        a.append(2)
        num1 = num1 // 2
    elif num1 % 3 == 0:
        num1 = num1 // 3
        a.append(3)
    else:
        break
        
mult = 1       
for k in range(len(a)):
    mult *= a[k]
    
if n*mult == m:
    print (len(a))
else:
    print (-1)
