import os
import random
import re
import subprocess
import argparse

# these three should work
binary_operators = ('+', '-', '*', '/', '%', '**', '//')
comparison_operators = ('<', '>', '<=', '>=', '==', '!=')
boolean_operators = ('and', 'or')

# how to mutate operators
binary_mutants = {
    '+': '-',
    '-': '+',
    '*': '/',
    '/': '*',
    '//': '*',
    '%': '/',
    '**': '*'
}
comparison_mutants = {
    '<': '<=',
    '<=': '<',
    '>': '>=',
    '>=': '>',
    '==': '!=',
    '!=': '=='
}
boolean_mutants = {
    'and': 'or',
    'or': 'and'
}
unary_mutants = {
    '+': '-',
    '-': '+'
}
not_mutants = {
    'not': ''
}

# not working
assignment_operators = ('=', '+=', '-=', '*=', '/=', '%=', '**=', '//=')
unary_operators = ('+', '-')
not_operators = ('not')

# not sure if these are implemented in mojo
# a potential issue is that tree-sitter-mojo considers bitwise operators binary operators
identity_operators = ('is', 'is not')
bitwise_operators = ('&', '|', '^', '<<', '>>')

# valid arguments
operator_types = ('boolean', 'binary', 'comparison', 'all', 'unary')


# function to validate arguments
def checker(arg):
    for a in arg:
        if a not in operator_types:
            raise argparse.ArgumentTypeError(f'{a} is not a valid operator\n'
                                             f' Valid: boolean, binary, comparison, all')
    return


# function to find position of operator in a line of the generated tree
# uses the last two numbers of the line to calculate the position
# this only works for single-digit numbers lol, handled in for loop
def find_op_position(line):
    numbers = re.findall(r'\d+', line)
    op_position = [int(num) for num in numbers][-2:]
    op_position[1] = op_position[1] - 3
    return op_position


# get cli arguments
parser = argparse.ArgumentParser(description='mojomut-gen')
parser.add_argument('filepath', help='mojo file to parse')
parser.add_argument('mutant_types', nargs='+',
                    help='valid mutant types (1 or more): all, binary, comparison, boolean')
filepath = parser.parse_args().filepath
mutant_types = parser.parse_args().mutant_types
checker(mutant_types)

# handles 'all'
if 'all' in mutant_types:
    mutant_types = ['binary', 'comparison', 'boolean']

# handles 'unary'
if 'unary' in mutant_types:
    mutant_types = mutant_types + ['not']

# make mutant directory
os.makedirs('mutants', exist_ok=True)

# generates parse tree using tree sitter
# this will fail if tree-sitter-mojo is not properly installed
result = subprocess.run(["npx", "tree-sitter", "parse", filepath], stdout=subprocess.PIPE)
string_out = result.stdout.decode("utf-8")

# generates mutants for each op type requested
for mutant_type in mutant_types:

    # the key to match operator type in tree
    if mutant_type != 'assignment':
        mutant = mutant_type + "_operator"
    else:
        mutant = 'assignment'

    # defines which operator/mutant list to reference
    match mutant_type:
        case 'binary':
            operators = binary_operators
            mutants = binary_mutants
        case 'comparison':
            operators = comparison_operators
            mutants = comparison_mutants
        case 'boolean':
            operators = boolean_operators
            mutants = boolean_mutants
        case 'unary':
            operators = unary_operators
            mutants = unary_mutants
        case 'not':
            operators = not_operators
            mutants = not_mutants
        # case 'assignment': operators = assignment_operators
        case _:
            operators = ()
            mutants = {}

    # finds lines with operators in the tree
    op_lines = [line for line in string_out.splitlines() if mutant in line]

    # get the op positions from lines w/operators
    op_positions = [find_op_position(line) for line in op_lines]
    mutant_ops = []

    # opens and reads original source code file
    with open(filepath, 'r') as file:
        original = file.readlines()

    # makes a copy of the file contents to mutate
    mutated = original.copy()

    # generates a mutant source code file for each mutant operator
    for idx, pos in enumerate(op_positions):
        is2CharOp = False
        is3CharOp = False
        mutated_line = mutated[pos[0]]

        # handles >1-character operands
        while (mutated_line[pos[1]] not in operators
               and mutated_line[pos[1] - 1] + mutated_line[pos[1]] not in operators
               and mutated_line[pos[1] - 2] + mutated_line[pos[1] - 1] + mutated_line[pos[1]] not in operators
        ):
            pos[1] -= 1
            if pos[1] < 0:
                break

        mutant_current = mutated_line[pos[1]]

        # handles 2-character operators
        if mutated_line[pos[1] - 1] + mutated_line[pos[1]] in operators:
            is2CharOp = True
            mutant_current = mutated_line[pos[1] - 1] + mutated_line[pos[1]]

        # handles 3-character operators ('and')
        if mutated_line[pos[1] - 2] + mutated_line[pos[1] - 1] + mutated_line[pos[1]] in operators:
            is3CharOp = True
            mutant_current = mutated_line[pos[1] - 2] + mutated_line[pos[1] - 1] + mutated_line[pos[1]]

        # decides which mutant to generate
        mutant_current = mutants.get(mutant_current)
        # swaps in the mutant operator
        if is2CharOp:
            mutated_line = mutated_line[:pos[1] - 1] + mutant_current + mutated_line[pos[1] + 1:]
        elif is3CharOp:
            mutated_line = mutated_line[:pos[1] - 2] + mutant_current + mutated_line[pos[1] + 1:]
        else:
            mutated_line = mutated_line[:pos[1]] + mutant_current + mutated_line[pos[1] + 1:]

        # swaps in the mutated line
        mutated[pos[0]] = mutated_line

        # writes the mutant file
        with open(f'mutants/{mutant_type}_mutant_{str(idx)}.🔥', 'w') as file:
            file.writelines(mutated)

        # resets current mutant operator for the next mutant file
        mutated[pos[0]] = original[pos[0]]
        print(f"{mutant_type} mutant {str(idx)} generated")
