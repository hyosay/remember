'''a = input()
print(a*2)'''


a, b = map(str, input().split())
if len(a) > len(b):
    print(len(a))
else:
    print(len(b))