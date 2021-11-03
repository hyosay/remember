n = int(input())
if n<1 or n>10000000:
    N=int(input())
else:
    count=0
    #n번 반복
    for i in range(1, n + 1):
        arr = []
        num=0
        # 약수를 구하는 알고리즘
        for j in range(1, i + 1):
            if i % j == 0:
                arr.append(j)
        print(arr)
# 정수의 합을 구하는 알고리즘
        n_str = str(i)
        for k in n_str:
            num += int(k)
# 신비한 수 구하는 알고리즘
        if num in arr:
            count += 1
    print(count)