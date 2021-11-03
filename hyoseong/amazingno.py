n = int(input())

count  = 0

# 4단계 n번 반복하기
for q in range(1, n + 1):
    arr = []
    num = 0
    #  1단계 약수를 구하는 알고리즘
    for i in range(1, q + 1):
        if q % i == 0:
            arr.append(i)

    # 2단계  정수의 합을 구하는 알고리즘
    n_str = str(q)

    for j in n_str:
        num += int(j)
    # 3단계 신비한 수를 구하는 알고리즘
    if num in arr:
        count += 1
    print("{}약수: {} 신비의 수: {}".format(q, arr, num))




