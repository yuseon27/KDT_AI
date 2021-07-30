## Hash
## https://school.programmers.co.kr/courses/11947/lessons/76995
## 완주하지 못한 선수

import collections

# Solution 1
def solution(participant, completion):
    return list(collections.Counter(participant) - collections.Counter(completion))

# Solution 2
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]

# Solution 3


def solution(participant, completion):
    d = {}
    for p in participant:  # {
        d[p] = d.get(p, 0) + 1
    #}
    for c in completion:  # {
        d[c] -= 1
    #}
    dnf = [k for k, v in d.items() if v > 0]
    return dnf[0]



participants = [["leo", "kiki", "eden"], ["marina", "josipa", "nikola", "vinko", "filipa"], ["mislav", "stanko", "mislav", "ana"]]
completion = [["eden", "kiki"], ["josipa", "filipa", "marina", "nikola"], ["stanko", "ana", "mislav"]]

for p, c in zip(participants, completion) :
    answer = solution(p, c)
    print(answer)



'''
["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]
'''
