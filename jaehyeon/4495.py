a= int(input())
b= int(input())
s =0
for j in range(a, b+1):
    arr = []
    for i in range(1, j+1):
        if j%i ==0:
            arr.append(i)
    s+=len(arr)
    print(arr)

print(s)