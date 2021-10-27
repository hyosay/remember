a, b = map(int, input().split())

count = 0
for i in range(a, b + 1): #1 ~ 10
    arr = []
    for j in range(1, i + 1):
        if i % j == 0:
            arr.append(j)
    print(arr)
    count += len(arr)

print(count)