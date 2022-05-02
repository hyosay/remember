def rank(n):
    if n<2:
        return 6
    elif n==2:
        return 5
    elif n==3:
        return 4
    elif n==4:
        return 3
    elif n==5:
        return 2
    else:
        return 1

def solution(lottos, win_nums):
    answer = []
    count = 0
    min_n = 0
    max_n = 0

    for i in lottos:
        if i ==0:
            count += 1
        elif i in win_nums:
            min_n += 1
    max_n = min_n + count

    answer.append(rank(max_n))
    answer.append(rank(min_n))

    return answer