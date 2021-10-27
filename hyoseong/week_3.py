
#약수를 구하는 알고리즘
a = int(input()) # 입력
arr = [] # 리스트 초기화
for i in range(1, a + 1):  # 1 ~ a까지 반복
    if a % i == 0: #나머지가 0이면 나누어지니깐 약수겠죠?
        arr.append(i) #그럼 arr리스트에 i를 추가

print(arr)

#힌트

#len() 으로 배열의 길이를 알 수 있습니다.

