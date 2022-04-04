#걍풀어봄
def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    answer = list(answer)
    answer.sort()
    return answer


#조합
from itertools import combinations

def solution(numbers):
    answer = []
    a = list(combinations(numbers, 2))

    for i in a:
        answer.append(i[0]+i[1])
    answer = list(set(answer))
    answer.sort()

    return answer

