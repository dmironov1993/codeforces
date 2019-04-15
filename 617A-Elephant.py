# https://codeforces.com/contest/617/problem/A

x = int(input())

steps = 0
while True:
    if x > 5:
        steps += x // 5
        x -= 5*(x // 5)
    else:
        for el in [1,2,3,4,5]:
            if x == el:
                steps += 1
                break
        break
        
print (steps)
