n = int(input())

queue = []
for i in range(n):
    inputValue = list(input().split())
    if inputValue[0] == 'i':
        queue.append(inputValue[1])
    elif inputValue[0] == 'o':
        if queue:
            print(queue.pop(0))
        else:
            print('empty')
    elif inputValue[0] == 'c':
        print(len(queue))