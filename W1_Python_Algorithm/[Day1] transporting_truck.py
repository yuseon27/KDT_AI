# from pythonds.basic.stack import Stack

def solution(max_weight, specs, names):
    answer = 0
    cnt = 0

    spec = {s[0]:int(s[1]) for s in specs}

    for name in names:  # {
        w = spec[name]
        if (cnt+w > max_weight) : #{
            answer += 1
            cnt = 0
        #}
        cnt += w
        print(cnt, answer)
    #}

    if cnt <= max_weight : answer += 1
    return answer

max_weights = [300, 200]
specs = [[["toy", "70"], ["snack", "200"]], [["toy", "70"], ["snack", "200"]]]
names = [["toy", "snack", "snack"], ["toy", "snack", "toy"]]

for w, s, n in zip(max_weights, specs, names) : #{
    answer = solution(w, s, n)
    print(answer)    
#}
