## Greedy
## https://school.programmers.co.kr/courses/11947/lessons/77004
## 큰 수 만들기

def solution(number, k):
    collected = []
    ## O(n)
    for i, num in enumerate(number):  # {
        while len(collected) > 0 and collected[-1] < num and k > 0:  # {
            collected.pop()
            k -= 1
        #}
        if k == 0:
            collected += list(number[i:])
            break
        collected.append(num)
    #}
    collected = collected[:-k] if k > 0 else collected

    return ''.join(collected)


def solution(number, k):
    answer = ''
    cnt = 0

    for n in number:  # {
        ## 새로운 값이 이전 값보다 크면
        while(cnt < k and len(answer) != 0 and answer[-1] < n):  # {
            answer = answer[:-1]
            cnt += 1
        #}
        answer += n
    #}

    ## k개 다 빨 때까지 뒤에서부터 삭제
    while(cnt < k):  # {
        answer = answer[:-1]
        cnt += 1
    #}

    return answer



## 시간 초과
from itertools import combinations

def solution(number, k):

    comb_list = list(combinations(number, len(number)-k))
    comb = [int(''.join(c)) for c in comb_list]

    return str(max(comb))


## 부분 정답
def solution(number, k):
    answer = ''

    for i in range(k):  # {
        max_v = max(number)
        max_idx = number.find(max_v)

        min_v = min(number[:max_idx+1])
        min_idx = number.find(min_v)
        number = number[:min_idx] + number[min_idx+1:]

        max_idx = number.find(max_v)
        if max_idx == 0:
            while(max_idx == 0):
                answer += max_v
                number = number[1:]
                max_idx = number.find(max_v)
    #}
    answer += number
    return answer
