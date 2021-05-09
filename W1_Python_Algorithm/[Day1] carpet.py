import math

def get_divisor(num) : #{
    divisor = []
    length = int(math.sqrt(num)) + 1

    for i in range(1, length) : #{
        if num % i == 0 : #{
            divisor.append([num//i, i])
        #}    
    #}
    divisor.sort()
    return divisor
#}

def solution(brown, red):
    answer = []
    divisor = get_divisor(brown+red)

    for d in divisor : #{
        w, h = d
        if (w-2)*(h-2) == red : #{
            answer = d
            break    
        #}
    #}
    return answer

color = [[10, 2], [8, 1], [24, 24]]
for c in color :
    answer = solution(c[0], c[1])
    print(answer)