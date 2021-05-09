import collections
'''
1. dictionary로 count하기
2. XOR 연산
3. zip 사용
'''

def solution(v):
    answer = [(s[0] ^ s[1] ^ s[2]) for s in zip(*v)]  ## 2
    answer = [s[2] if s[1] == s[0] else s[0] + s[1] - s[2] for s in zip(*v)]   ## 3

    return answer


vs = [[[1, 4], [3, 4], [3, 10]],
      [[1, 1], [2, 2], [1, 2]],
]

for v in vs : 
    ans = solution(v)
    print(ans)
