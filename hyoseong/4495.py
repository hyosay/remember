'''a= int(input())

count = 0
num = 0

# 4단계 n번 반복하기
for i in range(1, a + 1):
    arr = []
    num = 0
    # 1단계 약수를 구하는 알고리즘
    for j in range(1, i + 1):
        if i % j == 0:
            arr.append(j)
    # 2단계 정수의 합을 구하는 알고리즘
    str_i = str(i)
    for k in str_i:
       num += int(k)
    # 3단계 신비한 수를 구하는 알고리즘
    if num in arr:
        count += 1

print(count)'''

n = int(input())
count = 0
for i in range(1, n+1):
    k=0
    for j in str(i): # '13'
        k += int(j)

    if i % k == 0:
        count += 1
    print(k)
print(count)
