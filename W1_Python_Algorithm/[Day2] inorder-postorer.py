class ArrayStack:
    
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''

    for s in S : #{
        if s == '(' : opStack.push(s)
        elif s == ')':  # {
            while(opStack.peek() != '('):  # {
                answer += opStack.pop()
            #}
            opStack.pop()
        #}
        elif s in prec : #{
            if opStack.isEmpty() : opStack.push(s)
            else : #{
                if prec[opStack.peek()] < prec[s] : opStack.push(s)
                else : #{
                    while (not opStack.isEmpty() and prec[opStack.peek()] >= prec[s]) :  # {
                        answer += opStack.pop()  
                    #}
                    opStack.push(s)
                #}
            #}
        #}
        else : answer += s
    #}

    while(not opStack.isEmpty()) : #{
        answer += opStack.pop()    
    #}

    return answer


strings = ["(A+B)*(C+D)", "A*B+C", "A+B*C", "A+B+C", "(A+B)*C", "A*(B+C)", ]

for s in strings : #{
    print(s)
    answer = solution(s)
    print(answer)  
    print()
#}
