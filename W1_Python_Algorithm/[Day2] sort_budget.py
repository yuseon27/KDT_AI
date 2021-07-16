from itertools import combinations

def solution(d, budget):

    answer = 0
    done = 0
    d.sort()

    for item in d:  # {
        if done + item <= budget:  # {
            answer += 1
            done += item
        #}
        else:
            break
    #}

    # ## 시간 초과
    # for i in reversed(range(1, len(d)+1)) : #{
    #     comb = list(combinations(d, i))
    #     for c in comb : #{
    #         if sum(c) <= budget:
    #             return i
    #     #}
    # #}

    return answer

ds = [[1, 3, 2, 5, 4], [2, 2, 3, 3]]
budgets = [9, 10]
result = [3, 4]

for d, b in zip(ds, budgets) : #{
    answer = solution(d, b)    
    print(answer)
#}
