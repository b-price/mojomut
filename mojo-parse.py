import os
import random
import re
import subprocess
import argparse

BINARY_OPERATORS = ('+', '-', '*', '/', '%')


# function to find position of operator in a line of the generated tree
# uses the last two numbers of the line to calculate the position
# this only works for single-digit numbers lol
def find_op_position(line):
    numbers = re.findall(r'\d+', line)
    op_position = [int(num) for num in numbers][-2:]
    op_position[1] = op_position[1] - 3
    return op_position


# get cli arguments
parser = argparse.ArgumentParser(description='mojo-parse')
parser.add_argument('filepath', help='mojo file to parse')
filepath = parser.parse_args().filepath

# make mutant directory
os.makedirs('mutants', exist_ok=True)

# generates parse tree using tree sitter
# this will fail if tree-sitter-mojo is not properly installed
result = subprocess.run(["npx", "tree-sitter", "parse", filepath], stdout=subprocess.PIPE)
string_out = result.stdout.decode("utf-8")

# the kind of expression to mutate, binary arithmetic ops in this case
mutant = "binary_operator"

# finds lines with arithmetic operators in the tree
arithmetic_operators = [line for line in string_out.splitlines() if mutant in line]

# get the op positions from lines w/arithmetic ops
op_positions = [find_op_position(line) for line in arithmetic_operators]
mutant_ops = []

# creates a mutant operator for each operator found
# this is done randomly but should probably be smarter
for op_position in op_positions:
    mutant_ops.append(random.choice(BINARY_OPERATORS))

# opens and reads original source code file
with open(filepath, 'r') as file:
    original = file.readlines()

# makes a copy of the file contents to mutate
mutated = original

# generates a mutant source code file for each mutant operator
for idx, pos in enumerate(op_positions):
    mutated_line = mutated[pos[0]]
    # in the case of >1 digit number operands, finds the operator
    while mutated_line[pos[1]] not in BINARY_OPERATORS:
        pos[1] -= 1
        if pos[1] < 0:
            break

    mutated_line = mutated_line[:pos[1]] + mutant_ops[idx] + mutated_line[pos[1] + 1:]
    mutated[pos[0]] = mutated_line
    # writes the mutant file
    with open('mutants/mutant_' + str(idx) + '.mojo', 'w') as file:
        file.writelines(mutated)

    # resets current mutant operator
    mutated[pos[0]] = original[pos[0]]
