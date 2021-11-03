n = int(input())
arr = []

for i in range(n):
    arr.append((list(map(str, input().split()))))
print(arr)
stack_2 = []

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

# cd remember
# git pull
# git add .
# git commit -m 'week4'
# git push
# error
# git pull  후 다시 git push



