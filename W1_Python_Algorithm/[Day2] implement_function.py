import math

def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]

    standard = 0
    idx = 1
    cnt = 1

    while(idx < len(days)) : #{
        if days[standard] < days[idx] : #{
            answer.append(cnt)
            cnt = 1
            standard = idx
        #}
        else : #{
            cnt += 1
        #}
        idx += 1
    #}
    answer.append(cnt)
    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]

answer = solution(progresses, speeds)
print(answer)
