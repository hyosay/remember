'''from itertools import permutations

def solution(num):
    answer=[]
    num_list = list(permutations(num, len(num)))
    for num in num_list:
        answer.append(''.join(map(str,num)))

    return max(answer)'''

a= ['1', '3', '4']
print("".join(a))