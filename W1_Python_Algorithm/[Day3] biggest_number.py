## Sort
## https://school.programmers.co.kr/courses/11947/lessons/77001
## 가장 큰 수

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    numbers.sort(key=lambda x: x*4[:4], reverse=True)
    answer = str(int(''.join(numbers)))  ## int 하는 이유 : 만약에 numbers가 [0, 0] 등 0으로만 이루어져있다면 00이 아니라 0을 리턴해야함
    return answer
