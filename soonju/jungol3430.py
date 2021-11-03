n = int(input())
count = 0
for i in range(1, n+1):
    for j in str(i):
        k = sum([int(j)])
        if i % k == 0:
            count += 1
print(count)