n, m, k = map(int, input().split())
ans = 0

if n + k < m or k > m or max(n, m, k) > 30:
    print('Condition error')
else:
    stack = list(map(int, input().split()))
    stack = sorted(stack, reverse=True)
# 24 24 11
# 29 28 30 8 26 12 11 1 24 24 27 21 19 1 15 21 12 12 14 1 10 12 22 30
    if len(stack) == 0 or len(stack) > 30:
        print('Condition error')
    else:
        count = 1
        cnt = 0
        for i in range(m):
            if k == count:
                ans += stack[cnt]
                count = 0
                cnt += 1
            else:
                ans += stack[cnt]
            count += 1
        print(ans)
