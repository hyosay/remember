a = int(input())  # 층수
for i in range(1,a+1):
    for j in range(a-i):
        print(" ", end="")
    for j in range(1, i*2, i):
        print("*", end="")
    print("")
