# 0 ~ 9까지 한 줄로 출력
for i in range(10):
    print(i, end=' ')

print('\n'+'-' * 20)

# 짝수만 한 줄로 출력
for i in range(10):
    if i % 2 == 0:
        print(i, end=' ')

print( )

for i in range(5):
    print(2*i, end=' ')

print('\n'+'-' * 20)

# continue 와 pass
for i in range(1,11):
    if i > 5:
        pass
        print('i')
    l