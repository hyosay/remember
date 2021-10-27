n = int(input())

stack = 0

for j in range(n):
    c = []
    cont = 0
    if j == 0:
        c.append(0)
    for i in range(1, j + 1):
        if j % i == 0:
            c.append(i)
    a = str(j)
    for k in range(len(a)):
        cont += int(a[k])
    if cont in c:
        stack += 1

print(stack)



