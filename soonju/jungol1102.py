n = int(input())

stack = []
for i in range(n):
    inputValue = list(input().split())
    if inputValue[0] == 'i':   # 걍 쳐넣기
        stack.append(inputValue[1])    # 쌓임
    elif inputValue[0] == 'o':   # 안에 잇음
        if stack:
