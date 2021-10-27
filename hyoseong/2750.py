k, n, m = map(int, input().split())
arr = k * n - m
if m > k * n:
    print(0)
else:
    print(arr)