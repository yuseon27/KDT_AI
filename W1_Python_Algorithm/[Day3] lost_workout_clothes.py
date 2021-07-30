## Greedy
## https://school.programmers.co.kr/courses/11947/lessons/76998
## 체육복


# Solution 1
def solution(n, lost, reserve):
    s = set(lost) & set(reserve)
    re = set(reserve) - s
    l = set(lost) - s

    for r in sorted(re):
        if r-1 in l:
            l.remove(r-1)
        elif r+1 in l:
            l.remove(r+1)

    return n - len(l)

# Solution 2


def solution(n, lost, reserve):
    u = [1] * (n+2)
    for i in reserve:
        u[i] += 1
    for i in lost:
        u[i] -= 1

    for i in range(1, n+1):  # {
        if u[i-1] == 0 and u[i] == 2:
            u[i-1:i+1] = [1, 1]
        elif u[i+1] == 0 and u[i] == 2:
            u[i:i+2] = [1, 1]
    #}

    return len([x for x in u[1:-1] if x > 0])



nums = [5, 5, 3]
lost = [[2, 4], [2, 4], [3]]
reserve = [[1, 3, 5], [3], [1]]

for n, l, r in zip(nums, lost, reserve) : 
    answer = solution(n, l, r)
    print(answer)

'''
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]	4
3	[3]	[1]
'''
