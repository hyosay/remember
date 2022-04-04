'''
1 5 10 10 5 1
1 4 6 4 1
1 3 3 1

1 1 1 1 2 1 1 3 3 1 1 4 6 4 1
'''
c = int(input())
a = [1, 1, 1]
pivot = 2
for i in range(2, c): # 2
    a.append(1)
    pivot += 1
    for j in range(i - 1):
        a.append(a[pivot - i] + a[pivot - i + 1])
        pivot += 1
    pivot += 1
    a.append(1)

a_len = len(a)
for k in range(c, 0, -1):
    for i in range(a_len - 1, a_len - k - 1, -1):
        print(a[i], end=' ')
    a_len = a_len - k
    if a_len == 0:
        break
    print()