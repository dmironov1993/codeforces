# https://codeforces.com/contest/267/problem/A

n = int(input())
a = []
b = []
for _ in range(n):
    arr = list(map(int, input().split()))
    a.append(arr[0])
    b.append(arr[1])
    
    
for i in range(n):
    count = 0
    num1 = a[i]
    num2 = b[i]
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            count += num1 // num2
            num1 = num1 % num2
        else:
            count += num2 // num1
            num2 = num2 % num1
    print (count)
