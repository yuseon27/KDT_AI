from itertools import combinations

def solution(m, weights):
    answer = 0
    for i in range(1, len(weights)+1) :
        comb = list(combinations(weights, i))
        for c in comb : #{
            if sum(c) == m : answer += 1    
        #}

    return answer

m = 3000
weights = [500, 1500, 2500, 1000, 2000]

answer = solution(m, weights)
print(answer)