a, b = map(int, input().split())
c = int(input())
d = b+c
if d < 60:
    print("%d %d" %(a,d))
else :
    e = d // 60
    f = d % 60
    print("%d %d" %(a+e, f))