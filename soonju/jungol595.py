'''a = input()
print(a*2)'''

'''
a, b = map(str, input().split())
if len(a) > len(b):
    print(len(a))
else:
    print(len(b))'''

'''a = list(map(str, input().split()))
a.reverse()
print(a.)'''

'''a = list(map(int, input().split()))
print(a[0]+a[2]+a[4])'''

'''a = list(map(int, input().split()))
b = a[0::2]
c = a[1::2]
print("odd : %d" %sum(b))
print("even : %d" %sum(c))'''

'''n = int(input())
def a(n):
    for i in range(n):
        print("~!@#$^&*()_+|")
        return n
print(a)'''

'''def add(x):
    result = 0
    for i in range(1, x+1):
        result += i
    return result
print(add(100))'''

'''def sibal(x):
    for i in range(x+1):
        for j in range(x):'''


'''import numpy as np
a = list(map(int, input().split()))

print(sum(np.abs(a)))'''

'''a,b = map(int, input().split())
def sq(a,b):
    c = abs(a**2 - b**2)
    return c

print(sq(a,b))'''

'''N = int(input())
for _ in range(N):
    a = map(int, input().split())
    b = a.sort(reverse=True)
print(b)'''

'''a = [0 for i in range(4)]
n = int(input())
while n !=0:
    if n >=500:
        a[0]+=1
        n -= 500
    elif n >=100:
        a[1] +=1
        n -=100
    elif n >=50:
        a[2] +=1
        n -= 50
    elif n >=10:
        a[3] +=1
        n -= 10
print(a[0], a[1], a[2], a[3])'''

n,m,k = map(int, input().split())

if n+k < m:
    print('condition error')
else:
    a = list(map(int, input().split()))
    if len(a) == 0 or :
        print("condition error")
    else:
        a = sorted(a, reverse=True)

