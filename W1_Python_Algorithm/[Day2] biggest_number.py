def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key=lambda x : x*3, reverse=True)

    return str(int(''.join(numbers)))


numbers = [[6, 10, 2], [3, 30, 34, 5, 9], [505, 56, 54, 5, 55]]
for num in numbers : #{
    answer = solution(num)
    print(answer)    
#}
