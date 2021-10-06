import time
start_time = time.time()
a = [1,3, 5, 9, 15, 29, 35]

pl = 0
pr = len(a) - 1
pivot = (pl + (len(a) - 1)) // 2

chk = int(input())

while(1):
    if chk > a[pivot]:
        pl = pivot
        pivot = (pl + (len(a))) // 2
    elif chk == a[pivot]:
        print('%d'%(pivot))
        break
    elif chk < a[pivot]:
        pr = pivot
        pivot = (pl + pr) // 2



'''print(a.index(35))'''
end_time = time.time()

print('%.8f'%(end_time - start_time))

