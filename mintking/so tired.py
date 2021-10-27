a, b = map(int, input().split())
c = 0
while(b - a):
    if b % a ==0:
        c = c + a
    a = a + 1
print(c + b)