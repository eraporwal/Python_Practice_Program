from this import d


print("Program for infix to prefix and postfix....")
#a+b-c/d
#prefix
#+a-b/cd
#postfix
#dc/b-a+
#x='a+b-c/d'
# x='22+18-19/110'
# print(x)
# y=list(x)
# print(y)

def isOperator(c):
    return (not (c >= 'a' and c <= 'z') and not(c >= '0' and c <= '9') and not(c >= 'A' and c <= 'Z'))

def getPriority(C):
    if (C == '-' or C == '+'):
        return 1
    elif (C == '*' or C == '/'):
        return 2
    elif (C == '^'):
        return 3
    return 0

def infixToPrefix(infix):
    operators = []

    operands = []

    for i in range(len(infix)):

        if (infix[i] == '('):
            operators.append(infix[i])


        elif (infix[i] == ')'):
            while (len(operators)!=0 and operators[-1] != '('):
                # operand 1
                op1 = operands[-1]
                operands.pop()

                # operand 2
                op2 = operands[-1]
                operands.pop()

                # operator
                op = operators[-1]
                operators.pop()

                tmp = op + op2 + op1
                operands.append(tmp)

            operators.pop()

        elif (not isOperator(infix[i])):
            operands.append(infix[i] + "")

        else:
            while (len(operators)!=0 and getPriority(infix[i]) <= getPriority(operators[-1])):
                op1 = operands[-1]
                operands.pop()

                op2 = operands[-1]
                operands.pop()

                op = operators[-1]
                operators.pop()

                tmp = op + op2 + op1
                operands.append(tmp)
            operators.append(infix[i])

    while (len(operators)!=0):
        op1 = operands[-1]
        operands.pop()

        op2 = operands[-1]
        operands.pop()

        op = operators[-1]
        operators.pop()

        tmp = op + op2 + op1
        operands.append(tmp)

    return operands[-1]

s = input("enter a expression for convert in prefix : ")
print("Infix to prefix",infixToPrefix(s))

def infixToPostfix(expression): 

    stack = [] # initialization of empty stack

    output = '' 

    

    for character in expression:

        if character not in Operators:  # if an operand append in postfix expression

            output+= character

        elif character=='(':  # else Operators push onto stack

            stack.append('(')

        elif character==')':

            while stack and stack[-1]!= '(':

                output+=stack.pop()

            stack.pop()

        else: 

            while stack and stack[-1]!='(' and Priority[character]<=Priority[stack[-1]]:

                output+=stack.pop()

            stack.append(character)

    while stack:

        output+=stack.pop()

    return output
expression = input('Enter infix expression ')

print('infix notation: ',expression)

print('postfix notation: ',infixToPostfix(expression))
