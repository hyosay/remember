n = int(input('입력하실 명령의 수를 입력하시오. : '))
arr = []
for i in range(0,n+1):
    arr.append(list(map(str, input().split())))
print(arr)
stack_2=[]
for j in range(n):
    if arr[j][0] == 'i':
        stack_2.append(int(arr[j][1]))
    elif arr[j][0] == 'c':
        print(len(stack_2))
    elif arr[j][0] == 'o':
        if len(stack_2) == 0:
            print('empty')
        else:
            print(stack_2.pop())
