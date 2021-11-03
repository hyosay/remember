n = int(input())
stack = []
for i in range(n):
    stack.append((list(map(str, input().split()))))
stack_2 = []


for j in range(n):
    if stack[j][0] == 'i':
        stack_2.append(int(stack[j][1]))
    elif stack[j][0] == 'c':
        print(len(stack_2))
    elif stack[j][0] == 'o':
        if len(stack_2) == 0:
            print('empty')
        else:
            print(stack_2.pop(0))
