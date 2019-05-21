# https://codeforces.com/problemset/problem/1095/A?locale=en


n = int(input())
s = input()
i = 0
k = 1
count = 1
ans = ''
while True:
    if k <= n: 
        ans += s[i]
        count += 1
        i = k
        k +=  count
    else:
        break
print (ans)
