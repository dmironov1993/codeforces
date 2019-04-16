# https://codeforces.com/contest/339/problem/A

array = list(map(int, input().split('+')))

def BubbleSort(arr):
    for passnum in range(len(arr)-1,0,-1):
        for i in range(passnum):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                
BubbleSort(array)
print ('+'.join(list(map(str, array))))
