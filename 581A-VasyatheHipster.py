# https://codeforces.com/contest/581/problem/A
# https://codeforces.com/contest/581/submission/52599521

a,b = tuple(map(int, input().split()))

ans = []
if a > b:
    ans.append(b)
    ans.append((a-b)//2)
else:
    ans.append(a)
    ans.append((b-a)//2)
print (*ans)
