# https://codeforces.com/problemset/problem/71/A

n = int(input())

for i in range(n):
    word = input()
    k = len(word)
    if k > 10:
        print (word[0] + str(k-2) + word[-1])
    else:
        print (word)
