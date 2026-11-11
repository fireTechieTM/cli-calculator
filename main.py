from math import e, pi, tau

#Every substring allowed in the input split up
operations = ["+", "-", "*", "/", "^", "(", ")"]
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
predicates = []

#Take input
input = "2e2e25(6e.7)"
#Strip input of whitespace
input = input.replace(" ", "")

#All accepted mathematical operations, digits, constants, and predicates
math = set()
#Dictionary mapping constant names to float values
constants = {}

#Define 'math' and 'constants'
for i in range(0, 10):
  math.add(f"{i}")
  constants[f"{i}"] = i
math.add('.')

for i in ["e", "pi", "tau"]:
  math.add(i)
constants["e"] = e
constants["pi"] = pi
constants["tau"] = tau

for i in ["+", "-", "*", "/", "^", "(", ")"]:
  math.add(i)

#List of mathematical operations, digits, constants, and predicates being worked with
operands = []


#Input: string 'input' all w symbols in 'math', 'operands' an empty list
#Output: all symbols in 'input' parsed into separate elements in 'operands'
#takes the first symbol in 'math' it sees in the current substring
#ex. input = "abccc", math = {"abc", "abcc", "abccc", "c", "cc"} -> operands = ["abc", "c", "c"]
#Error(s): If a current substr is not in 'math', it will grow to include the rest of 'input'
def parse_input_to_operands(input, operands):
  i = 0
  curr = ""
  while i < len(input):
    curr += input[i]
    
    eol = (i == len(input) - 1) # end of list
    #Assumes that last substr of 'input' is an operand in 'math'
    if eol == True:
      operands.append(curr)
      break
      
    prefix_count = sum(item.startswith(curr) for item in math) # num vals in 'math' that 'curr' prefixes
    next_prefix_count = sum(item.startswith(curr + input[i + 1]) for item in math) # num vals in 'math' that 'curr' plus next element of 'input' prefixes
    operand_identified = (prefix_count == 1 and next_prefix_count == 0) or (prefix_count > next_prefix_count) # whether an operand match for 'curr' has been chosen from 'math'

    #'curr' is valid, so add it to operands and reset it
    if operand_identified:
      operands.append(curr)
      curr = ""
        
    i += 1

  return operands


operands = parse_input_to_operands(input, operands)

#Input: list of strings
#Output: list of errors found in 'operands'
def catch_operand_errors(operands):
  error_report = []
  
  num_parens = 0
  for i in operands:
    if i == '(': 
      num_parens += 1
    elif i == ')':
      num_parens -= 1

  if num_parens != 0:
    error_report.append("INVALID PARENTHESES")

  for i in operands:
    if i not in math:
      error_report.append("INVALID OPERAND")
      break

  if error_report == []:
    return ["NO ERRORS"]
  else:
    return error_report
  
# operand_errors = catch_operand_errors(operands)
# print(operand_errors)


#Input: list of strings, all in 'math' 
#Output: replaces all strings of 'operands' which are in 'constants' with their numeric values
def emplace_operands(operands):
    new_operands = []

    i = 0
    while i < len(operands):
        if operands[i] in digits or operands[i] == '.':
            num = operands[i]
            i += 1
            while i < len(operands) and (operands[i] in digits or operands[i] == '.'):
                num += operands[i]
                i += 1
            new_operands.append(float(num))
            continue

        if operands[i] in constants:
          new_operands.append(constants[operands[i]])
        else:
          new_operands.append(operands[i])
        
        i += 1

    return new_operands


#Driver
operands = emplace_operands(operands)
print(input)
for i in range(0, len(operands)):
  print(operands[i],end="")
print()
print(operands)


def exponent(operands):
  return operands

def multiplication_division(operands):
  new_operands = []

  i = 0
  while i < len(operands):
    if type(operands[i]) is float:
      num = operands[i]
      i += 1
      while i < len(operands) and (type(operands[i]) is float):
        num *= operands[i]
        i += 1
      new_operands.append(float(num))
      i += 1
        

  return new_operands



def addition_subtraction(operands):
  return operands

def simplify_defined_constants(operands):
  operands = exponent(operands)
  operands = multiplication_division(operands)
  operands = addition_subtraction(operands)
  return operands

operands = simplify_defined_constants(operands)
print(operands)