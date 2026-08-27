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

accepted_operations = ['*', '/', '+', '-']
accepted_quantities = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def simplify(operands):
    # _operands = []
    i = 0
    while i < len(operands) - 1:
        if operands[i + 1] == '*':
            operands[i] *= operands[i + 2]
            operands.remove(operands[i + 2])
            operands.remove('*')
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
            current = ""
            while i < len(equation) and equation[i] in accepted_quantities: 
                current += equation[i]
                i += 1
            operands.append(int(current))
        i += 1

    return simplify(operands)


print(solve(equation, 0, False))