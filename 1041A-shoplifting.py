# https://codeforces.com/contest/1041/problem/A

n = int(input())
arr = list(map(int, input().split()))

#print (max(arr) - min(arr) + 1 - n)

def BubbleSort(n, arr):
    for passnum in range(n-1,0,-1):
        for i in range(passnum):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

BubbleSort(n, arr)
print (arr[-1] - arr[0] + 1 - n)
