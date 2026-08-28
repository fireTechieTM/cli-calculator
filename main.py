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


global_position = 0
def solve(equation, position=0): 
    operands = []

    while position < len(equation):
        if equation[position] == '(':
            parentheses_solution = solve(equation, position + 1)
            operands.append(parentheses_solution[0])
            position = parentheses_solution[1]
        elif equation[position] == ')':
            for operation in accepted_operations:
                operands = simplify(operands, operation)
            return operands[0], position

        elif equation[position] in accepted_operations:
            operands.append(equation[position])
        elif equation[position] in accepted_quantities:
            current = equation[position]
            while position + 1 < len(equation) and equation[position + 1] in accepted_quantities:
                position += 1
                current += equation[position]
            operands.append(int(current))
        position += 1

    for operation in accepted_operations:
        operands = simplify(operands, operation)

    return operands[0]

print(solve(equation))