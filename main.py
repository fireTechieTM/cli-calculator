equation = input("""
Use this four function calculator as you would use any.\n
You may use parentheses as well as:\n
+ for addition, - for subtraction\n
* for multiplication, / for division\n
What do you need calculated? (whitespace is acceptable)\n
""")

#What is the solution?
#4 * 3 * 12
#First, we must split it up recursively

accepted_operations = ['*', '/', '+', '-'] #must be in order of operations
accepted_quantities = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def simplify(operands, operation):
    i = 0
    while i < len(operands) - 1:
        if operands[i + 1] == operation:
            if operation == '*': operands[i] *= operands[i + 2]
            if operation == '/': operands[i] /= operands[i + 2]
            if operation == '+': operands[i] += operands[i + 2]
            if operation == '-': operands[i] -= operands[i + 2]
            operands.remove(operands[i + 2])
            operands.remove(operation)
        else:
            i += 1
    return operands

def solve(equation, position, in_parentheses):
    #something

    operands = []
    i = 0

    while i < len(equation):
        if equation[i] in accepted_operations:
            operands.append(equation[i])
        elif equation[i] in accepted_quantities:
            current = equation[i]
            while i + 1 < len(equation) and equation[i + 1] in accepted_quantities:
                i += 1
                current += equation[i]
            operands.append(int(current))
        i += 1

    for operation in accepted_operations:
        operands = simplify(operands, operation)
        
    return operands

print(solve(equation, 0, False))