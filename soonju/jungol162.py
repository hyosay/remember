c = list(map(int, input().split()))
for i in range(8):
    c.append((c[i]+c[i+1]) % 10)

for j in c:
    print(j, end=" ")