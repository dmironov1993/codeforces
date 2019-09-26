t = int(input())
for i in range(t):
    k = int(input())
    a = [*map(int, input().split())]
    mv = 10**9
    count = 0
    for x in reversed(a):
        if x > mv : count += 1
        mv = min(mv, x)
    print (count)
