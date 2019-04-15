# https://codeforces.com/problemset/problem/705/A

first = 'I hate'
second = 'I love'
sentence = 'I hate'
turn = 0
n = int(input())
if n == 1:
    print (sentence + ' it')
else:
    for _ in range(n-1):
        if turn == 0:
            turn = 1
            sentence += ' that ' + second
        else:
            turn = 0
            sentence += ' that ' + first
    sentence += ' it'
    print (sentence)
