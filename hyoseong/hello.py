'''거스름돈 주기 [조건문과 연산자]
설명
당신은 편의점 알바생이다. 포스기에는 거스름돈으로 사용할500원, 100원, 50원, 10원짜리 동전이 있다. 손님에게 거슬러 줘야 할 돈이 N원 일 경우 입력 N에 대해 잔돈을 거슬러 주는 프로그램을 작성하라.

조건: 잔돈은 큰 단위부터 거슬러 준다.

입력
입력 N은 0이상 10000이하의 수를 입력받는다.

출력
왼쪽 부터 500원, 100원, 50원, 10원 순으로 자연수만 출력한다.
자연수는 공백으로 구분되며 맨마지막 자연수 뒤에는 공백이 붙지 않는다.'''


N = int(input())
money = [500, 100, 50, 10]
stack = [0,0,0,0]

for j, i in enumerate(money):
    stack[j] = N // i
    N %= i


for i in stack:
    print(i, end=' ')



