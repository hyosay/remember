#시간이 오래 걸린다.
A,B=map(int,input('숫자 범위 지정').split())
count=0
for i in range(A,B+1):
    arr = []                #밖에다 하면 축적이 된다. 따라서 안에다 해야한다.
    for j in range(1,i+1):
        if i % j == 0:
            arr.append(j)
    print(arr)              #각각의 약수 출력
    count += len(arr)       #약수 개수 구하기
print(count)                # A~B사이의 총 약수 개수 출력