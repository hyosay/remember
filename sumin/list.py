list = [1,2,3]
list.append(5)
list.extend([4,5])
print(list)
del list[0] # 인덱스 0에 해당하는 요소 제거
list.pop(2) # 인덱스 2에 해당하는 요소 제거
list.remove(5) # 값 5에 해당하는 요소 제거
print(list)

for _ in range(3): # 굳이 할당할필요가 없기 때문에 i를 안쓰고 _를 썼다
    print(0)

n, m = map(int, input().split())
a = [list(map(int,input())) for _ in range(n)]
# 공백을 기준으로 정수값을 입력받아 list로 만들어줌 이걸 n번 반복하여 2차원으로 저장함
print(a) # 공백없이 입력받기

'''111
   010
   011
'''