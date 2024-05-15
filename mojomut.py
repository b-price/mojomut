import os
import random
import re
import subprocess
import argparse
import shutil

# tuples of operators
binary_operators = ('+', '-', '*', '/', '%', '**', '//', '>>', '<<', '^', '&', '|')
# I don't think 'is not' is correctly mutated
comparison_operators = ('<', '>', '<=', '>=', '==', '!=', 'is', 'is not')
boolean_operators = ('and', 'or')
unary_operators = ('+', '-')
not_operators = ('not')

# how to mutate operators
binary_mutants = {
    '+': '-',
    '-': '+',
    '*': '/',
    '/': '*',
    '//': '*',
    '%': '/',
    '**': '*',
    '>>': '<<',
    '<<': '>>',
    '|': '&',
    '&': '|',
    '^': '|'
}
comparison_mutants = {
    '<': '<=',
    '<=': '<',
    '>': '>=',
    '>=': '>',
    '==': '!=',
    '!=': '==',
    'is': 'is not',
    'is not': 'is'
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

# valid arguments
mutant_args = ('boolean', 'binary', 'comparison', 'unary', 'all', 'integer', 'operator')


# function to validate cli arguments
def checker(arg):
    for a in arg:
        if a not in mutant_args:
            raise argparse.ArgumentTypeError(f'{a} is not a valid mutant type\n'
                                             f' Valid: boolean, binary, comparison, unary, all, integer, operator')
    return


# function to find position of operator in a line of the generated tree
# uses the last two numbers of the line to calculate the position
# this only works for single-digit operands lol, handled in for loop
def find_op_position(line):
    numbers = re.findall(r'\d+', line)
    op_position = [int(num) for num in numbers][-2:]
    op_position[1] = op_position[1] - 2
    return op_position


# function to find integer positions
def find_int_position(line):
    numbers = re.findall(r'\d+', line)
    int_position = [int(num) for num in numbers][-4:]
    int_position[1] = int_position[1]
    int_position[3] = int_position[3]
    return int_position


# function to generate integer mutants
def integer_replacement(num):
    choice = random.randrange(1, 6)
    match choice:
        case 1:
            return num + 1
        case 2:
            return num - 1
        case 3:
            return num * 2
        case 4:
            return num * 10
        case 5:
            return num + 10
        case 6:
            return num * -1
        case _:
            return num + 2


# get cli arguments
parser = argparse.ArgumentParser(description='mojomut')
parser.add_argument('filepath', help='mojo file to mutate')
parser.add_argument('mutant_types', nargs='+',
                    help='valid mutant types (1 or more): all, binary, comparison, unary, boolean, integer')
filepath = parser.parse_args().filepath
mutant_types = parser.parse_args().mutant_types
checker(mutant_types)

# handles 'unary'
if 'unary' in mutant_types:
    mutant_types = mutant_types + ['not']

# handles 'operator'
if 'operator' in mutant_types:
    mutant_types = ['binary', 'comparison', 'boolean', 'unary', 'not']

# handles 'all'
if 'all' in mutant_types:
    mutant_types = ['binary', 'comparison', 'boolean', 'unary', 'not', 'integer']

# make mutant directory
os.makedirs('tests', exist_ok=True)
mutant_dirs = []

# generates parse tree using tree sitter
# this will fail if tree-sitter-mojo is not properly installed
# add npm/npx/whatever package manager that works for you as the first argument if you don't want to use the binary
result = subprocess.run(["tree-sitter", "parse", filepath], stdout=subprocess.PIPE)
string_out = result.stdout.decode("utf-8")

# generates mutants for type requested
for mutant_type in mutant_types:

    # the key to match mutant type in tree
    if mutant_type != 'integer':
        mutant = mutant_type + "_operator"
    else:
        mutant = 'integer'

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

    # opens and reads original source code file
    with open(filepath, 'r') as file:
        original = file.readlines()

    # makes a copy of the file contents to mutate
    mutated = original.copy()

    # finds lines with requested mutant types in the tree
    mut_lines = [line for line in string_out.splitlines() if mutant in line]

    # get the mutant positions from lines w/mutant types
    if mutant_type == 'integer':
        mut_positions = [find_int_position(line) for line in mut_lines]
    else:
        mut_positions = [find_op_position(line) for line in mut_lines]

    # generates a mutant source code file for each potential mutant
    for idx, pos in enumerate(mut_positions):
        mutated_line = mutated[pos[0]]

        # handles integers
        if mutant_type == 'integer':
            mutant_current = ''
            # finding the exact positions of the integers is easy
            for position in range(pos[1], pos[3]):
                mutant_current += mutated_line[position]

            # creates and swaps in mutated integers
            mutant_current = integer_replacement(int(mutant_current))
            mutated_line = mutated_line[:pos[1]] + str(mutant_current) + mutated_line[pos[3]:]

        # handles operators
        else:
            is2CharOp = False
            is3CharOp = False

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

            # handles 3-character operators
            if mutated_line[pos[1] - 2] + mutated_line[pos[1] - 1] + mutated_line[pos[1]] in operators:
                is2CharOp = False
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

        # makes folder for mutant
        mutant_str_pos = f'{pos[0] + 1}-{pos[1] + 1}'
        mutant_folder = f'tests/mojomut_mutant_{mutant_type}_{mutant_str_pos}'
        os.makedirs(mutant_folder, exist_ok=True)
        mutant_dirs.append(mutant_folder)
        shutil.copyfile(f'test_{filepath}', f'{mutant_folder}/test_{filepath}')

        # writes the mutant file
        with open(f'{mutant_folder}/{filepath}', 'w') as file:
            file.writelines(mutated)

        # resets current mutant for the next mutant file
        mutated[pos[0]] = original[pos[0]]
        print(f"{mutant_type} mutant {str(idx + 1)} generated")

# runs pytest on tests against mutants
print('Pytest-Mojo running...')
test_result = subprocess.run(["pytest", "tests/"], stdout=subprocess.PIPE)
string_output = test_result.stdout.decode("utf-8")

# prints pytest output. parsed for mutant info below
print(string_output)

# this commented out code is for considering each test case rather than each test
# fail_str = string_output.split('=========================== short test summary info ============================')

# results = [line for line in fail_str[1].splitlines()]

# failpass = [int(i) for i in results[len(results) - 1].split() if i.isdigit()]

# results = results.pop()

# if len(failpass) > 2:
#     mutation_score = 0
# else:
#     mutation_score = failpass[0]/ (failpass[0] + failpass[1])

# print(f'Mutation Score: {mutation_score * 100}%')
# print(f'Mutants Survived: {failpass[1]}')
# print(f'Mutants Killed: {failpass[0]}')
# print('Mutants survived at:')
# for line in results:
#     linesplit = line.split(":: ")
#     print(linesplit[1])


# here the mutant score is calculated by number of mutants killed
# splits pytest output into the lines with results
split_output = string_output.split('\n\n')
results = [line for line in split_output[1].splitlines()]

# list of positions of survived mutants, count of killed mutants
survived = []
killed = 0

# loop to parse result lines for survivors
for result in results:
    result_split = result.split(' ')
    if 'F' not in result_split[1]:
        survived.append(re.findall(r'\d+', result_split[0]))
    else:
        killed += 1

mutation_score = killed / len(results)

# Mojomut output
print(f'Mutation Score:     {mutation_score * 100:.2f}%')
print(f'Mutants Survived:   {len(survived)}')
print(f'Mutants Killed:     {killed}')
if len(survived) > 0:
    print('Mutants survived at:')
    for survivor in survived:
        print(f'Line {survivor[0]}, Column {survivor[1]}')

# deletes all the mutants
# ignore_errors prevents a bug where it tries to delete a mutant twice
for dir in mutant_dirs:
    shutil.rmtree(dir, ignore_errors=True)
