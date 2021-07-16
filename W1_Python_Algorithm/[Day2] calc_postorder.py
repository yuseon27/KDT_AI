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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for t in tokenList : #{
        if t == '(' : opStack.push(t)
        elif t == ')' : #{
            while(opStack.peek() != '(') : #{
                postfixList.append(opStack.pop())    
            #}
            opStack.pop()
        #}
        elif t in prec : #{
            if opStack.isEmpty() : opStack.push(t)
            else : #{
                if prec[opStack.peek()] < prec[t] : opStack.push(t)
                else : #{
                    while(not opStack.isEmpty() and prec[opStack.peek()] >= prec[t]) : #{
                        postfixList.append(opStack.pop())    
                    #}
                    opStack.push(t)
                #}
            #}
        #}
        else : postfixList.append(t)
    #}

    while(not opStack.isEmpty()) : postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList): #{
    numStack = ArrayStack()

    for t in tokenList : #{
        if isinstance(t, int) : numStack.push(t)
        else : #{
            b = numStack.pop()
            a = numStack.pop()

            if   t == '+' : c = a + b
            elif t == '-' : c = a - b
            elif t == '*' : c = a * b
            elif t == '/' : c = a / b

            numStack.push(c)
        #}
    #}
    return numStack.pop()
#}


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val


equation = ["5 + 3", 	"(1 + 2) * (3 + 4)", "7 * (9 - (3+2))"]

for eq in equation : #{
    answer = solution(eq)    
    print(eq, answer)
    # exit()
#}
