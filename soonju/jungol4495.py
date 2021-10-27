a, b = map(int, input().split())
arr = []
brr = []
for i in range(1, a):
    if a % i == 0:
        arr.append(i)
for i in range(1, b+1):
    if b % i == 0:
        brr.append(i)
print(len(brr)-len(arr))