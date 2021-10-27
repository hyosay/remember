a, b = map(int, input().split())

count = 0

for i in range(a, b+1):       #a부터 b사이의 수
    arr = []
    for j in range(1, i+1):
        if i % j == 0:
            arr.append(i)
    #print(arr)
    count += len(arr)

print(count)


#arra = []
#arrb = []

#for i in range(1, a+1):
#    if a%i==0:
#        arra.append(i)

#for j in range(1, b+1):
#    if b%j==0:
#        arrb.append(j)

#lena = (len(arra))
#lenb = (len(arrb))

#print(lena + lenb)